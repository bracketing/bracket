from test_route import test_app_route as app_create


def test_build():
    app = app_create()

    app.config.setconfig("BUILD_OUTPUTDIR","./_bracket")

    app.build()
