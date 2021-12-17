import requests
from bs4 import BeautifulSoup
from transliterate import translit
import urllib.request
from db import crud, models
from loguru import logger

log = logger
log.add("log.log", level="DEBUG", rotation="500 MB")


class CantFindWord(Exception):
    pass


class PageError(Exception):
    pass


class CantFindTranslation(Exception):
    pass


class CantFindAudioSource(Exception):
    pass


def get_text_from_page(url: str):
    response = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36", })

    if response.status_code == 404:
        raise CantFindWord

    if response.status_code != 200:
        raise PageError

    return response.text


def get_word_info(db_word: models.Word):
    """
    :param db_word: Слово на русском
    """

    root = "http://www.ganiev.org"
    word_translate_url = root + "/ru/words/"

    word_english = translit(db_word.russian_word, language_code="ru", reversed=True)

    text = get_text_from_page(url=word_translate_url + word_english)

    soup = BeautifulSoup(text, "lxml")

    translation = soup.find("div", class_="word_description")
    if not translation:
        raise CantFindTranslation

    translation = translation.text.strip()

    if translation[:2] == "1.":
        translation = translation[2:].strip()

    translation = ", ".join([t.strip() for t in translation.split(",")])

    audio_source = soup.find("div", class_="audio-src")
    if not audio_source:
        raise CantFindAudioSource
    audio_source = audio_source.attrs["data-src"]
    urllib.request.urlretrieve(root + audio_source, f"data/{word.id}.mp3")

    crud.set_translation(word.id, tatar_word=translation)
    print(f"Добавил перевод: {word.russian_word} - {translation}")


for word in crud.get_words():
    # Пропускаем слова, у которых уже есть перевод
    if word.tatar_word:
        continue

    try:
        get_word_info(word)
    except CantFindTranslation:
        log.info(f"Не удается найти перевод для слова {word.russian_word}")
    except CantFindAudioSource:
        log.info(f"Не удается найти аудио для слова {word.russian_word}")
    except CantFindWord:
        crud.delete_word(word.id)
        log.info(f"Не удается найти слово {word.russian_word}")
    except PageError:
        log.info(f"Какая-то ошибка на сайте со словом {word.russian_word}")
