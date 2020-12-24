from jinja2 import Template
import bracket

if __name__ == "__main__":
    app = bracket.WebSite(__name__)

    @app.pages("/")
    def helloworld(context):
        return context({
        "title":"Welcome to Bracket",
        "content":Template('''
            <h1>{{ messages }}</h1>
            <img src="{{ bracket.res('/logo.png')}}">
        '''),
        "resources":{
            "messages":"Welcome to Bracket"
        }
    })

    @app.pages("/user")
    def userindex(context):
        return context({
        "title":"User Index",
        "content":Template('''
            <div align="center">
                <h1>{{ messages }}</h1>
            </div>
        '''),
        "resources":{
            "messages":"User Index"
        }
    })

    app.serve()