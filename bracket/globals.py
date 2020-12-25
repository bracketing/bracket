# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""
from werkzeug.local import Local, LocalProxy
from .context import PagesContext


l = Local()


# All Context
pages = PagesContext
resources = LocalProxy(l, 'resources')