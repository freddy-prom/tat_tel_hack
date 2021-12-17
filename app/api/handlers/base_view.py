from aiohttp.web import View


class BaseView(View):
    @property
    def db(self):
        return self.request.app['db']

    @property
    def client_session(self):
        return self.request.app['client_session']

    @property
    def oauth_token(self):
        return self.request.app['oauth_token']

    @property
    def direct_base_url(self):
        return self.request.app['direct_base_url']
