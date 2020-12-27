# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""

from jinja2 import Template

simpleTemplate = """<!DOCTYPE html>
<html lang="{{ objdict['lang'] }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="generator" content="Bracket ({{ objdict['bracketVersion'] }}) & Jinja2 ">
    {{ objdict['headermeta'] }}
    <title>{{ objdict['title'] }}</title>
</head>
<body>
    <div id="bracketapp">
        {{ objdict['content'] }}
    </div>
</body>
</html>"""


def getSimplePages(objdict):
    dispatch = Template(simpleTemplate).render({"objdict": objdict})
    return dispatch
