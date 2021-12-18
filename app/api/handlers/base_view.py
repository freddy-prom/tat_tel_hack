from aiohttp.web import View


class BaseView(View):
    @property
    def client_session(self):
        return self.request.app['client_session']

