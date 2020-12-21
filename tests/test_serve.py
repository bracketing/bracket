from test_route import test_app_route as app_route

def test_app_serve():
    app = app_route()

    app.serve()