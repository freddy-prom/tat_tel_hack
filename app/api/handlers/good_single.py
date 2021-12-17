from http import HTTPStatus
from aiohttp.web import json_response

from app.api.handlers.base_view import BaseView
from app.api.schemas.request_schemas import AddGoodRequestSchema
from app.db.crud import NotFound


class GoodSingle(BaseView):
    URL = '/api/v1/goods/{good_id}'

    async def get(self):
        good_id = get_int_id_from_str(self.request.match_info['good_id'])
        good = await self.db.get_good(good_id)

        if good is None:
            return json_response(
                status=HTTPStatus.NOT_FOUND
            )

        return json_response(
            status=HTTPStatus.OK,
            data=good
        )

    async def patch(self):
        good_id = get_int_id_from_str(self.request.match_info['good_id'])

        parsed_request = await AddGoodRequestSchema.parse_validate_request(
            self.request)
        try:
            await self.db.update_good(
                good_id=good_id,
                name=parsed_request.body.name,
                description=parsed_request.body.description,
                image=parsed_request.body.image,
                price=parsed_request.body.price,
                active=parsed_request.body.active,
                count=parsed_request.body.count,
            )
        except NotFound:
            return json_response(
                status=HTTPStatus.NOT_FOUND
            )

        return json_response(
            status=HTTPStatus.OK
        )

    async def delete(self):
        good_id = get_int_id_from_str(self.request.match_info['good_id'])
        try:
            await self.db.delete_good(good_id)
        except NotFound:
            return json_response(
                status=HTTPStatus.NOT_FOUND
            )

        return json_response(
            status=HTTPStatus.OK
        )


def get_int_id_from_str(good_id: int):
    try:
        return int(good_id)
    except ValueError:
        raise
