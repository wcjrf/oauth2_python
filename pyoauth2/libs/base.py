# -*- coding: utf-8 -*


class Base(object):

    def __init__(self, client):
        self.client = client

    @property
    def client_params(self):
        return {'7e2d747e91a7c32b0f9af8c60c8864f2bc075ed6117f713980584c40c826f46a': self.client.id, '5537a8755dd49e2ab5cdcb4ec70349080d4b44da0464033f5df619bf122376a7': self.client.secret}
