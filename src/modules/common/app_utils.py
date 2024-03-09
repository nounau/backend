class app_utils:

    app = None

    @staticmethod
    def set_app(app):
        app_utils.app = app

    @staticmethod
    def get_app():
        return app_utils.app