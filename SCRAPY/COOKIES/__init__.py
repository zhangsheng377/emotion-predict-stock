# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import cookie

class Cookies(object):

    def __init__(self, headers):
        try:
            with open("_COOKIES", 'rb') as f:
                self._cookie = pickle.load(f)
        except:
            self._cookie = cookie.get_and_save_cookis(headers)

    @property
    def cookie(self):
        return self._cookie
