# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""
from .context import PagesContext
from .configs import Configs, default_configs
from .debug import serve as debug
import importlib
import os


class WebSite(object):
    def __init__(self, import_name, import_modules={}):
        self.import_name = import_name
        self.import_modules = import_modules

        self.pages_list = []
        self.resources_list = []

        self.config = Configs()
        self.config_default = default_configs

    def add_page(self, rule, viewfunc):
        if not rule.startswith("/"):
            raise NameError("The route must start with a forward slash.")

        self.pages_list.append({"rule": rule, "viewfunc": viewfunc})

    def add_resource(self, func):
        self.resources_list.append(func)

    def pages(self, rule):
        def decorator(f):
            self.add_page(rule=rule, viewfunc=f)
            return f

        return decorator

    def resources(self):
        def decorator(f):
            self.add_resource(func=f)
            return f

        return decorator

    def dispatch(self, route):

        dispatchs = None

        for obj in self.pages_list:
            if obj["rule"] == route:
                dispatch = obj["viewfunc"](PagesContext)
                if isinstance(dispatch, PagesContext):
                    dispatchs = dispatch.render()
                else:
                    dispatchs = dispatch

        return dispatchs

    def serve(self, serveconfig=None):
        if not serveconfig:
            serveconfig = {
                "host": self.config.get("SERVE_HOST"),
                "port": self.config.get("SERVE_PORT"),
                "debug": self.config.get("SERVE_DEBUG"),
            }
        print("Running on http://localhost:" + str(serveconfig["port"]))
        debug(self, serveconfig)

    def escape(self, url: str):
        if not url.startswith("/"):
            raise NameError("The url must start with a forward slash.")

        if url == "/":
            url = "/index"

        return url + ".html"

    def build(self):

        print("Building Staticfile with you ...")

        try:
            os.mkdir(self.config.get("BUILD_OUTPUTDIR"))
        except:
            pass

        for view in self.pages_list:
            static = self.dispatch(view["rule"])
            if static == None:
                continue

            filepath = self.config.get("BUILD_OUTPUTDIR") + self.escape(view["rule"])

            with open(filepath, "w+", encoding="utf-8") as file:
                file.write(str(static))

            print("Every thing was Ok.")
