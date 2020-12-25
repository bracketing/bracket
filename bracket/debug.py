# -*- coding: utf-8 -*-
"""
    bracket
    ~~~~~

    Bracket is an Elegant static site generator.

    :copyright: (c) 2020 by Ceorleorn(https://github.com/ceorleorn).
    :license: MIT License, see LICENSE for more details.
"""
import importlib

def serve(app,serveconfig):
    try:
        flask = importlib.import_module("flask")
    except:
        raise RuntimeError("Flask is not installed.")
        
    app = flask.Flask("Bracket",static_url_path="/static")
        
    @app.route("/",methods=["GET","POST"])
    def indexhandler():
        dispatch = app.dispatch("/")
        if not (dispatch == None):
            return dispatch
        else:
            return flask.abort(404)

    @app.route("/<url>",methods=["GET","POST"])
    def otherurlhandler(url):
        dispatch = app.dispatch("/" + url)
        if not (dispatch == None):
            return dispatch
        else:
            return flask.abort(404)
        
    app.run(port=serveconfig["port"])