# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .senta_snownlp import SentaSnownlp


def SentaFactory(model="snownlp"):
    if model == "snownlp":
        return SentaSnownlp()
    else:
        raise ValueError('model name: {} can not find.'.format(model))
        pass
    return None
