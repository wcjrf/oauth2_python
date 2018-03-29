# -*- coding: utf-8 -*-

from pyoauth2.libs import utils
from pyoauth2.libs.utils import urlencode


class Connection(object):

    def __repr__(self):
        return '<OAuth2 Connection>'

    @classmethod
    def build_url(cls, url, path='', params={}):
        params = urlencode(params)
        params = '?%s' % params if params else ''
        url = path if path.startswith(('http://', 'https://')) else '%s%s' % (url, path)
        return '%s%s' % (url, params)
