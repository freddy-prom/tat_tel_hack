import time

import requests
from bs4 import BeautifulSoup
from db import crud


class PageNotFound(Exception):
    pass


class PageError(Exception):
    pass


class CantFindTranslation(Exception):
    pass


class CantFindAudioSource(Exception):
    pass


def get_page(url: str):
    response = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36", })

    if response.status_code == 404:
        raise PageNotFound

    if response.status_code != 200:
        raise PageError

    return response.text


def get_words_from_page():
    pass


def get_last_page_for_letter(url: str) -> int:
    response = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})

    soup = BeautifulSoup(response.text, "lxml")

    pagination = soup.find("ul", class_="pagination")
    if not pagination:
        return 1

    items = pagination.find_all("li")
    assert items
    pages = []
    for item in items:
        a = item.find("a")
        if not a:
            continue
        pages.append(a.text)

    assert pages[-1].isnumeric(), f"На {url} не удается найти последнюю страницу"
    return int(pages[-1])


def get_words_from_url(letter: str):
    for page in range(1, letters_and_pages[letter] + 1):
        response = requests.get(
            url=root_url + letter,
            headers={
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"},
            params={"page": page})

        print(f"Взял запрос по {response.url}")

        soup = BeautifulSoup(response.text, "lxml")
        divs = soup.find_all("div", class_="col-sm-3 col-xs-6")

        for div in divs:
            ul = div.find("ul", class_="list-unstyled")
            for word_url in ul.find_all("a"):
                crud.add_word(word_url.text.strip())

        print(f"Добавил все слова по {response.url}")

        sleep_time = 1
        print(f"Заснул на {sleep_time}")
        time.sleep(sleep_time)


root_url = "https://wordsonline.ru/"

letters_and_pages = {
    'А': 35, 'Б': 41, 'В': 67, 'Г': 34, 'Д': 45, 'Е': 3, 'Ё': 1,
    'Ж': 7, 'З': 46, 'И': 29, 'Й': 1, 'К': 66, 'Л': 23, 'М': 48,
    'Н': 65, 'О': 76, 'П': 182, 'Р': 52, 'С': 94, 'Т': 39, 'У': 26,
    'Ф': 18, 'Х': 13, 'Ц': 7, 'Ч': 11, 'Ш': 14, 'Щ': 2, 'Э': 15, 'Ю': 2, 'Я': 3}

for m_letter in letters_and_pages.keys():
    get_words_from_url(m_letter)
