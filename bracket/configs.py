# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""

default_configs = {
    "BUILD_OUTPUTDIR": "./docs",
    "BUILD_DEBUG": False,
    "I18N_OPEN": False,
    "I18N_DATA": {"zh-CN"},
    "SERVE_HOST": "localhost",
    "SERVE_PORT": 5000,
    "SERVE_DEBUG": False,
}


class Configs(object):
    def __init__(self):
        self.configs = default_configs

    def setconfig(self, name, value):
        self.configs[name] = value

    def delete(self, name):
        del self.configs[name]

    def get(self, name):
        try:
            return self.configs[name]
        except:
            return None
