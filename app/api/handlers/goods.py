from http import HTTPStatus

from aiohttp import web

from app.api.handlers.base_view import BaseView
from app.api.schemas.request_schemas import AddGoodRequestSchema


class Goods(BaseView):
    URL = '/api/v1/goods'

    async def get(self):
        goods_list = await self.db.get_all_goods()

        return web.json_response(
            status=HTTPStatus.OK,
            data=goods_list
        )

    async def post(self):
        parsed_request = await AddGoodRequestSchema.parse_validate_request(self.request)
        good_as_json = await self.db.create_good(
            name=parsed_request.body.name,
            description=parsed_request.body.description,
            image=parsed_request.body.image,
            price=parsed_request.body.price,
            active=parsed_request.body.active,
            count=parsed_request.body.count
        )

        return web.json_response(
            status=HTTPStatus.OK,
            data={
                'id': good_as_json
            }
        )
