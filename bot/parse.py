import requests
from bs4 import BeautifulSoup
from transliterate import translit
import urllib.request


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


def get_word_info(word: str):
    """
    :param word: Слово на русском
    """

    root = "http://www.ganiev.org"
    word_translate_url = root + "/ru/words/"

    word_english = translit(word, language_code="ru", reversed=True)

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
    urllib.request.urlretrieve(root + audio_source, f"data/{word_english}.mp3")

    return translation


words = ["мама", "папа", "суп", "хлеб", "ресторан"]

for word in words:
    print(get_word_info(word))
