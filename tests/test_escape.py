from test_app import test_app_create as app_create


def test_escape():
    app = app_create()

    if app.escape("/") != "/index.html":
        raise ValueError("Escape is error.")

    if app.escape("/hello") != "/hello.html":
        raise ValueError("Escape is error.")
