# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""

from .app import WebSite
from .context import PagesContext
from .pages import getSimplePages

from .info import __version__


__all__ = [
    "WebSite",
    "PagesContext",
    "getSimplePages"
    "__version__"
]
