# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Cookies(object):

    def __init__(self, headers):
        self._headers = headers
        try:
            with open("_COOKIES", 'rb') as f:
                self._cookie = pickle.load(f)
        except:
            self._cookie = self.new_cookie()

    @property
    def cookie(self):
        return self._cookie

    def new_cookie(self):
        from . import cookie
        self._cookie = cookie.get_and_save_cookis(self._headers)
        return self._cookie
