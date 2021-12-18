from http import HTTPStatus
from random import shuffle

from aiohttp.web import json_response

from api.handlers.base_view import BaseView
from db import crud


class FindExcess(BaseView):
    URL = "/api/v1/game/find_excess/{count}"

    async def get(self):

        count = str(self.request.match_info["count"])
        if not count.isnumeric():
            return json_response(
                status=HTTPStatus.BAD_REQUEST,
                data={"message": "Incorrect count"})
        else:
            count = int(count)

        excesses = crud.get_all_excesses()
        shuffle(excesses)
        return json_response(
            status=HTTPStatus.OK,
            data=excesses[:count])
