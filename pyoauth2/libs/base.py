# -*- coding: utf-8 -*


class Base(object):

    def __init__(self, client):
        self.client = client

    @property
    def client_params(self):
        return {'client.id': self.client.id, 'client.secret': self.client.secret}
