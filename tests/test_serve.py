from test_route import test_app_route as app_route

def test_app_serve():
    app = app_route()
    
    #app.serve()
    return app

if __name__ == "__main__":
    test_app_serve().serve()