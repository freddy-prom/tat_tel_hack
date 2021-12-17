from http import HTTPStatus
from aiohttp.web import json_response

from app.api.handlers.base_view import BaseView
from app.api.schemas.request_schemas import AddGoodRequestSchema
from app.db.crud import NotFound


class