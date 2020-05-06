# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def DataBaseFactory(database_name, sheet_name, model="pymongo"):
    '''树莓派只能通过pip安装pymongo==3.2版本
    '''
    if model == "pymongo":
        from .database_pymongo import DataBasePyMongo
        return DataBasePyMongo(database_name=database_name, sheet_name=sheet_name)
    else:
        raise ValueError('model name: {} can not find.'.format(model))
        pass
    return None
