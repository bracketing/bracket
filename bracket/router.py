# Router
from .helpers import _BracketClass
from .helpers import exampleTemplateFunc


class Router(_BracketClass):
    def __init__(self,route,viewfunc,templatefunc=exampleTemplateFunc):
        self.route = route
        self.viewfunc = viewfunc
        self.templatefunc = templatefunc

    def render(self,templatefunc):
    
        dispatch = self.viewfunc(pages={
            "url":route,
        })
        return self.templatefunc(dispatch)


def route(url,template=exampleTemplateFunc,**options):
    def decorator(f):
        return Router(router=url,viewfunc=f,templatefunc=template)
    return decorator