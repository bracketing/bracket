from test_route import test_app_route as app


def test_dispatch():
    website = app()

    return website.dispatch("/")
