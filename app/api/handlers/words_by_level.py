from http import HTTPStatus
from aiohttp.web import json_response

from api.handlers.base_view import BaseView
from db import crud


class LevelWords(BaseView):
    URL = "/api/v1/dictionary/words/level/{level_number}"

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

        return json_response(
            status=HTTPStatus.OK,
            data=crud.get_words_by_level(level_number))
