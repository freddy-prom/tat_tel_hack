from http import HTTPStatus

from aiohttp import web
from pydantic import ValidationError


@web.middleware
async def middleware_exception(request, handler):
    try:
        response = await handler(request)
    except web.HTTPException:
        raise
    except ValidationError:
        return web.json_response({'message': 'bad-parameters'},
                                 status=HTTPStatus.BAD_REQUEST)
    except ValueError:
        return web.json_response(
            {'message': 'incorrect value'},
            status=HTTPStatus.BAD_REQUEST
        )
    except Exception as e:
        return web.json_response({'message': str(e)},
                                 status=HTTPStatus.INTERNAL_SERVER_ERROR)
    return response
