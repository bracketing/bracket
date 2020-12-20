# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""


class WebSite(object):
    def __init__(self, import_name, import_modules={}):
        self.import_name = import_name
        self.import_modules = import_modules

        self.pages_list = []
        self.resources_list = []
    
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