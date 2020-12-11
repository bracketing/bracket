# APP

from .router import Router
from .helpers import _BracketClass
import os

class Bracket(_BracketClass):
    def __init__(self,import_name):
        self.router = {}

    def install(self,obj):
        if isinstance(obj,Router):
            is_same = True
            try:
                self.router[obj.route]
            except:
                is_same = False
            if not is_same:
                self.router[obj.route] = obj
            else:
                raise "Router namespace is hard."
    
    def serve(configs):
        pass