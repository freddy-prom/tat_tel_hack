from http import HTTPStatus
from aiohttp.web import json_response

from api.handlers.base_view import BaseView
from db import crud
import random


class RandomWord(BaseView):
    URL = "/api/v1/dictionary/words/random/{count}"

    async def get(self):
        try:
            count = int(self.request.match_info["count"])
        except:
            return json_response(
                status=HTTPStatus.BAD_REQUEST,
                data={"message": "Cant get count"}
            )

        if count <= 0:
            return json_response(
                status=HTTPStatus.BAD_REQUEST,
                data={"message": "Count less than zero"})

        words = crud.get_words()

        if count > len(words):
            count = len(words)

        return json_response(
            status=HTTPStatus.OK,
            data=random.sample(words, k=count))
