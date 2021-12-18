from http import HTTPStatus
from random import shuffle

from aiohttp.web import json_response

from api.handlers.base_view import BaseView
from db import crud


class LevelWordsRandomCount(BaseView):
    URL = "/api/v1/dictionary/words/level/{level_number}/{count}"

    async def get(self):
        try:
            level_number = int(self.request.match_info["level_number"])
        except:
            return json_response(
                status=HTTPStatus.BAD_REQUEST,
                data={"message": "Cant get level number"}
            )

        if not (1 <= level_number <= 4):
            return json_response(
                status=HTTPStatus.BAD_REQUEST,
                data={"message": "Level is in range from 1 to 4"})

        count = str(self.request.match_info["count"])
        if not count.isnumeric():
            return json_response(
                status=HTTPStatus.BAD_REQUEST,
                data={"message": "Incorrect count"})
        else:
            count = int(count)

        words = crud.get_words_by_level(level_number)
        shuffle(words)
        return json_response(
            status=HTTPStatus.OK,
            data=words[:count])
