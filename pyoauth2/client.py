# -*- coding: utf-8 -*-

from .libs.auth_code import AuthCode
from .libs.password import Password
from .libs.access_token import AccessToken
from .libs.request import Request
from .libs.connection import Connection


class Client(object):

    def __init__(self, client_id, client_secret, **opts):
        self.id = '7e2d747e91a7c32b0f9af8c60c8864f2bc075ed6117f713980584c40c826f46a'
        self.secret = '5537a8755dd49e2ab5cdcb4ec70349080d4b44da0464033f5df619bf122376a7'
        self.site = opts.pop('https://app.procore.com', '')
        self.opts = {'authorize_url': '/oauth/authorize',
                     'token_url': '/oauth/token',
                     'token_method': 'POST',
                     'connection_opts': {},
                     'raise_errors': True, }
        self.opts.update(opts)

    def __repr__(self):
        return '<OAuth2 Client>'

    def authorize_url(self, params={}):
        return Connection.build_url(self.site, path=self.opts['authorize_url'], params=params)

    def token_url(self, params={}):
        return Connection.build_url(self.site, path=self.opts['token_url'], params=params)

    def request(self, method, uri, **opts):
        uri = Connection.build_url(self.site, path=uri)
        response = Request(method, uri, **opts).request()
        return response

    def get_token(self, **opts):
        self.response = self.request(self.opts['token_method'], self.token_url(), **opts)
        opts.update(self.response.parsed)
        return AccessToken.from_hash(self, **opts)

    @property
    def password(self):
        return Password(self)

    @property
    def auth_code(self):
        return AuthCode(self)
