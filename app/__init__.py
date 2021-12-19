import aiohttp
from aiohttp import web
import os
import ssl
from api.handlers import handlers
from api.middleware import middleware_exception

PORT = os.environ.get('PORT', 5000)
HOST = os.environ.get('HOST', 'tel-hackathon.ru')


async def on_start(app: web.Application):
    app['connection_on'] = True
    app['client_session'] = aiohttp.ClientSession()


async def on_shutdown(app: web.Application):
    await app['client_session'].close()


def create_app():
    app = web.Application(middlewares=[middleware_exception])

    app.on_startup.append(on_start)
    app.on_shutdown.append(on_shutdown)

    app['oauth_token'] = 'AQAAAAAoPF1mAAd_WI72IH3Q5UJuu4DxHHcEP9g'
    app['direct_base_url'] = 'https://api-sandbox.direct.yandex.com/json/v5'
    for handler in handlers:
        app.router.add_route('*', handler.URL, handler)
    return app


def main():
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    crt = "/etc/letsencrypt/live/tel-hackathon.ru/fullchain.pem"
    key = "/etc/letsencrypt/live/tel-hackathon.ru/privkey.pem"
    ssl_context.load_cert_chain(crt, key)
    app = create_app()
    web.run_app(app, port=PORT, host=HOST, ssl_context=ssl_context)


if __name__ == '__main__':
    main()
