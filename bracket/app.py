# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""
from .context import PagesContext, StaticContext
from .configs import Configs, default_configs
from .debug import serve as debug
import importlib
import os


class WebSite(object):
    def __init__(self, import_name, import_modules={}):
        """
        Main application objects of bracket.

        ===================================
        from bracket import WebSite

        app = WebSite(__name__)
        ===================================

        """
        self.import_name = import_name
        self.import_modules = import_modules

        self.pages_list = []
        self.resources_list = []
        self.extensions_list = []

        self.config = Configs()
        self.config_default = default_configs

    def add_page(self, rule, viewfunc):
        """
        Add the underlying interface of interface view function.

        ===================================
        from bracket import WebSite
        from jinja2 import Template

        app = WebSite(__name__)

        def hello(context):
            return context({
                "title":"Welcome!!!",
                "content":Template('''<h1>Hello</h1>'''),
                "resources":{}
            })

        app.add_page("/",hello)
        ===================================

        """
        if not rule.startswith("/"):
            raise NameError("The route must start with a forward slash.")

        self.pages_list.append({"rule": rule, "viewfunc": viewfunc})

    def add_resource(self, func):
        """
        Add the underlying interface of static resources.

        ===================================
        from bracket import WebSite
        from jinja2 import Template

        app = WebSite(__name__)

        def hello(static):
            return static([])

        app.add_resources("/",hello)
        ===================================

        """
        self.resources_list.append(func)

    def pages(self, rule):
        """
        Add interface view function.

        ===================================
        from bracket import WebSite
        from jinja2 import Template

        app = WebSite(__name__)

        @app.pages("/")
        def hello(context):
            return context({
                "title":"Welcome!!!",
                "content":Template('''<h1>Hello</h1>'''),
                "resources":{}
            })

        ===================================

        """

        def decorator(f):
            self.add_page(rule=rule, viewfunc=f)
            return f

        return decorator

    def resources(self):
        """
        Add interface static resources.

        ===================================
        from bracket import WebSite
        from jinja2 import Template

        app = WebSite(__name__)

        @app.resources("/")
        def hello(static):
            return static([])

        ===================================

        """

        def decorator(f):
            self.add_resource(func=f)
            return f

        return decorator

    def dispatch(self, route):
        """
        Render the interface view function that has been added.

        ===================================
        from bracket import WebSite
        from jinja2 import Template

        app = WebSite(__name__)

        @app.pages("/")
        def hello(context):
            return context({
                "title":"Welcome!!!",
                "content":Template('''<h1>Hello</h1>'''),
                "resources":{}
            })

        app.dispatch("/")

        ===================================

        They return:

        ===================================

        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="generator" content="Bracket (0.0.1) & Jinja2 ">

            <title>Welcome!!!</title>
        </head>
        <body>
            <div id="bracketapp">
                <h1>Hello</h1>
            </div>
        </body>
        </html>

        ===================================

        """
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
        """
        Use Flask to preview the current web site.

        $ pip install flask

        ===================================
        from bracket import WebSite
        from jinja2 import Template

        app = WebSite(__name__)

        @app.pages("/")
        def hello(context):
            return context({
                "title":"Welcome!!!",
                "content":Template('''<h1>Hello</h1>'''),
                "resources":{}
            })

        app.serve()

        ===================================

        They output and running on http://localhost:5000/

        ===================================

        Running on http://localhost:5000
          * Serving Flask app "Bracket" (lazy loading)
          * Environment: production
            WARNING: This is a development server. Do not use it in a production deployment.
            Use a production WSGI server instead.
          * Debug mode: off
          * Running on http://localhost:5000/ (Press CTRL+C to quit)

        ===================================

        """
        if not serveconfig:
            serveconfig = {
                "host": self.config.get("SERVE_HOST"),
                "port": self.config.get("SERVE_PORT"),
                "debug": self.config.get("SERVE_DEBUG"),
            }
        print("Running on http://localhost:" + str(serveconfig["port"]))
        debug(self, serveconfig)

    def escape(self, url: str):
        """
        Convert route to file path.

        ===================================
        from bracket import WebSite

        app = WebSite(__name__)

        app.escape("/")
        >>> "/index.html"

        app.escape("/hello")
        >>> "/hello.html"

        ===================================

        """
        if not url.startswith("/"):
            raise NameError("The url must start with a forward slash.")

        if url == "/":
            url = "/index"

        return str(url + ".html")

    def build(self):
        """
        Render the interface view function that has been added.

        ===================================
        from bracket import WebSite
        from jinja2 import Template

        app = WebSite(__name__)

        @app.pages("/")
        def hello(context):
            return context({
                "title":"Welcome!!!",
                "content":Template('''<h1>Hello</h1>'''),
                "resources":{}
            })

        app.build()

        ===================================

        They return and saved file:

        ===================================

        Building Staticfile with you ...

        Every thing was Ok.

        ===================================s

        gitpod /workspace/bracket/docs $ ls
        >>>index.html

        ===================================

        """
        print("Building Staticfile with you ...\n")

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

    def loader_extension(self, extension):
        """
        Load extension object.

        ===================================
        from bracket import WebSite

        class Extension(object):
            def __init__(self,configs):
                self.configs = configs
                self.moduels = {"createLink": self.createLink}

            def createLink(self,text,link):
                return Template('''<a href="{{ link }}">{{ text }}</a>''').render(text=text,link=link)

        app = WebSite(__name__)

        app.loader_extension(Extension)
        ===================================

        """
        if not isinstance(extension, object):
            raise TypeError("Extension must be a object.")

        if not hasattr(extension, "modules"):
            raise TypeError("Missing attribute: modules.")

        if not isinstance(extension.moduels, dict):
            raise TypeError("Modules must be a dict.")

        self.extensions_list.append(extension)

    def loader_resources(self):
        """
        Load all static resources that have been added

        ===================================
        from bracket import WebSite

        app = WebSite(__name__)

        @app.resources("/")
        def hello(static):
            return static([
                {"filename":"link.txt","content":"bracket.ink"}
            ])

        app.loader_resources()
        ===================================

        """
        resources = []
        for loaderfunc in self.resources_list:
            dispatch = loaderfunc(StaticContext)
            for resource in dispatch:
                resources.append(resource)
        return resources
