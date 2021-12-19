from http import HTTPStatus
from typing import List

from aiohttp.web import json_response
from fuzzywuzzy import fuzz

from api.handlers.base_view import BaseView
from db import crud


class LikeWords(BaseView):
    URL = "/api/v1/dictionary/words/{word}"

    async def get(self):
        word = self.request.match_info["word"]
        return json_response(
            status=HTTPStatus.OK,
            data=get_like_words(word))


def get_like_words(russian_word: str) -> List[dict]:
    words = crud.get_words()
    answer = []
    for word in words:
        if check_similarity(word["russian_word"], russian_word):
            answer.append(word)
    return answer


def check_similarity(word_one: str, word_two: str):
    ratio = fuzz.WRatio(word_two, word_one)
    return ratio > 80