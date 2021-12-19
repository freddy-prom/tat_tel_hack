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

    async def post(self):
        request = await self.request.json()
        if not all([type(i) == int for i in request]):
            return json_response(
                status=HTTPStatus.BAD_REQUEST,
                data={"message": "Id in list must be integer"}
            )
        res = []
        for word_id in request:
            word = crud.get_word(word_id)
            res.append(word)

        return json_response(
            status=HTTPStatus.OK,
            data=res)
