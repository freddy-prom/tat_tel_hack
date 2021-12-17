from json import JSONDecodeError

from aiohttp.web import Request
from pydantic import BaseModel, Field, validator


class BaseRequestSchema(BaseModel):
    class BodySchema(BaseModel):
        pass

    class QuerySchema(BaseModel):
        pass

    body: BodySchema
    query: QuerySchema

    @classmethod
    async def parse_validate_request(cls, request: Request):
        try:
            request_body = await request.json()
        except JSONDecodeError:                                    # empty body
            request_body = {}

        request_as_dict = {
            'body': request_body,
            'query': request.query,
        }

        return cls.parse_obj(request_as_dict)
