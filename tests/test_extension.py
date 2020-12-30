from jinja2 import Template
from bracket import WebSite

def createLink(text,link):
    return Template('''<a href="{{ link }}">{{ text }}</a>''').render(text=text,link=link)

class Extension(object):
    def __init__(self,configs):
        self.__name__ = "example"
        self.configs = configs
        self.createLink = createLink


def test_app_extension_loader():
    app = WebSite(__name__)
    app.loader_extension(Extension)
    return app

def test_app_extension_runincontext():
    app = test_app_extension_loader()

    @app.pages("/")
    def hello(context):
        return context({
            "title":"Welcome",
            "content":Template('''{{ example.createLink("go to Github","https://github.com") }}'''),
            "resources":app.loader({})
        })
    
    return app.dispatch("/")


