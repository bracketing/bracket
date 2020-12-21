from test_app import test_app_create as app_create

from bracket import PagesContext
from jinja2 import Template

def test_context_pages():
    context = PagesContext({
        "title":"Welcome to Bracket",
        "content":Template('''
            <h1>{{ messages }}</h1>
            <img src="{{ bracket.res('logo.png')}}">
        '''),
        "resources":{
            "messages":"Welcome to Bracket"
        }
    })
    
    return context