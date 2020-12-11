from ..components import helloworld

from bracket import route

@route
def index(pages):
    return helloworld.helloworld(props={})