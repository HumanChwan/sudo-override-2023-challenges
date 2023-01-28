from flask import Flask

# Blueprint Import
from apps.userApp.views import userApp


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object('config.DevelopmentConfig')
    app.register_blueprint(userApp)
    
    return app


if __name__ == '__main__':
    create_app().run()