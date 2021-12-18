from http import HTTPStatus
from aiohttp.web import json_response

from api.handlers.base_view import BaseView


class Ping(BaseView):
    URL = "/api/v1/ping"

    async def get(self):
        return json_response(
            status=HTTPStatus.OK, data={"message":"pong"})
