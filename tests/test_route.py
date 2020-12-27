from test_app import test_app_create as app_create
from jinja2 import Template
import bracket


def test_app_route():
    app = app_create()

    @app.pages("/")
    def helloworld(context):
        return context(
            {
                "title": "Welcome to Bracket",
                "content": Template(
                    """
            <h1>{{ messages }}</h1>
            <img src="{{ bracket.res('/logo.png')}}">
        """
                ),
                "resources": {"messages": "Welcome to Bracket"},
            }
        )

    return app
