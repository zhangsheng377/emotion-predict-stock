# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random


class Agents(object):

    def __init__(self):
        from . import agents
        self._agents = agents.agents

    @property
    def agents(self):
        return self._agents

    def get_random_agent(self):
        return random.choice(self._agents)
