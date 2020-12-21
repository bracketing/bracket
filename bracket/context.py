# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""
from jinja2 import Template
from .info import __version__


class PagesContext(object):
    def __init__(self, objdict):
        try:
            objdict["title"]
            objdict["content"]
        except:
            raise ValueError("The return value is missing a required key.")

        if not isinstance(objdict["title"], str):
            raise TypeError("The title must be a string.")

        if not isinstance(objdict["content"], Template):
            raise TypeError("The content must be a jinja2.Template.")

        self.objdict = objdict
        self.title = objdict["title"]
        self.content = objdict["content"]

    def generateContext(self):
        return {
            "bracket": RenderContext({
                "version": str(__version__),
                "title": self.objdict["title"]
            }),
            "i18n":None
        }
    
    def render(self):
        dispatch = self.content.render(self.generateContext())
        return str(dispatch)



class RenderContext(object):
    def __init__(self, attribute={}):
        for attr, value in attribute.items():
            setattr(self, attr, value)

    def res(self,url,file_type=None):
        return "/static/" + url

    def find(self,filepath):
        return 0
    
    def url(self,url):
        return 0
