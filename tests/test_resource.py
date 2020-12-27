from test_app import test_app_create as app_create
import bracket


def test_app_resource():
    app = app_create()

    @app.resources()
    def resources(static):
        return static([
            {"filename":"link.txt","content":"bracket.ink"}
        ])

    return app
