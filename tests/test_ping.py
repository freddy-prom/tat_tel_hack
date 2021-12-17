from http import HTTPStatus

from pytest import fixture

from app import create_app


@fixture
async def test_client(aiohttp_client):
    app = create_app()
    return await aiohttp_client(app)


async def test_ping(test_client):
    resp = await test_client.get('/ping')
    assert resp.status == HTTPStatus.OK
