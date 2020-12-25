# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""
from werkzeug.local import Local, LocalManager
from .context import PagesContext
from .debug import serve as debug
import importlib

class WebSite(object):
    def __init__(self, import_name, import_modules={}):
        self.import_name = import_name
        self.import_modules = import_modules

        self.pages_list = []
        self.resources_list = []

        self.local = Local()
        self.local_manager = LocalManager([self.local])

        
    
    def add_page(self,rule,viewfunc):
        if not rule.startswith("/"):
            raise ValueError("The route must start with a forward slash.")

        self.pages_list.append({
            "rule":rule,
            "viewfunc":viewfunc
        })
    
    def add_resource(self,func):
        self.resources_list.append(func)
    
    def pages(self, rule):
        def decorator(f):
            self.add_page(rule=rule,viewfunc=f)
            return f

        return decorator
    
    def resources(self):
        def decorator(f):
            self.add_resource(func=f)
            return f

        return decorator
    
    def dispatch(self,route):

        dispatchs = None

        self.local.resources = {
            "ext":self.import_modules
        }

        for obj in self.pages_list:
            if obj["rule"] == route:
                dispatch = obj["viewfunc"](PagesContext)
                if isinstance(dispatch,PagesContext):
                    dispatchs = dispatch.render()
                else:
                    dispatchs = dispatch

        self.local_manager.cleanup()

        return dispatchs
            
    def serve(self,serveconfig={
        "port":5000
    }):

        debug(self,serveconfig)
