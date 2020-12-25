# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""
from jinja2 import Template
from .pages import getSimplePages
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

        self.objdict = self.checkUIObjDict(objdict)

        self.title = objdict["title"]
        self.content = objdict["content"]
        self.headermeta = objdict["ui"]["headermeta"]
        self.lang = objdict["ui"]["lang"]
    
    def checkUIObjDict(self,objdict):
        checkitems = {
            "headermeta":"",
            "lang":"zh-CN",
            "description":"A simple pages",
            "keywords":"bracket,web,page",
            "author":"user"
        }

        try:
            objdict["ui"]
        except:
            objdict["ui"] = {}

        for itemsname, itemsvalue in checkitems.items():
            try:
                objdict["ui"][itemsname]
            except:
                objdict["ui"][itemsname] = itemsvalue

        return objdict

    def generateContext(self):
        try:
            res = self.objdict["resources"]
        except:
            res = {}

        context = {
            "bracket": RenderContext({
                "version": str(__version__),
                "title": self.objdict["title"]
            }),
            "i18n":None
        }

        for obj,value in res.items():
            i = False
            try:
                context[obj]
                i = True
            except:
                i = False
            if i:
                raise NameError("Resource name is same.")
            context[obj] = value

        return context


    def render(self,template=getSimplePages):
        dispatch = self.content.render(self.generateContext())

        objdict = {
            "title":self.title,
            "headermeta":self.headermeta,
            "lang":self.lang,
            "content":dispatch,
            "bracketVersion":__version__
        }

        return str(template(objdict))



class RenderContext(object):
    def __init__(self, attribute={}):
        for attr, value in attribute.items():
            setattr(self, attr, value)

    def res(self,url:str,file_type=None):
        if not url.startswith("/"):
            raise NameError("The resource name must start with a forward slash.")

        return "/static" + url
    
    def url(self,url):
        return 0

class ResourcesContext(object):
    def __init__(self,install_resources):
        self.install_resources = install_resources
    
    def install(self,name,resources):
        if not self.isInstalled(name):
            self.add(name,resources)
        else:
            raise NameError("Resource name is same.")
    
    def add(self,name,resources):
        self.install_resources[name] = resources
    
    def isInstalled(self,name):
        i = False
        try:
            self.install_resources[name]
            i = True
        except:
            i = False
        return i