from http import HTTPStatus

from aiohttp import web

from .base_view import BaseView


class Ping(BaseView):
    URL = r'/ping'

    async def get(request: web.Request) -> web.Response:
        return web.json_response({'message': 'connected'},
                                 status=HTTPStatus.OK)


class PingDb(BaseView):
    URL = r'/ping_db'

    async def get(self) -> web.Response:
        await self.db.ping_db()
        return web.json_response({'message': 'db connected'},
                                 status=HTTPStatus.OK)
