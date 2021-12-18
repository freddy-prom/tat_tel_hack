from http import HTTPStatus
from aiohttp.web import json_response

from api.handlers.base_view import BaseView
from db import crud


class AllWords(BaseView):
    URL = "/api/v1/dictionary/words/all"

    async def get(self):
        return json_response(
            status=HTTPStatus.OK,
            data=crud.get_words())
