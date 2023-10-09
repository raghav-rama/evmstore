from flask import Flask
from config import Config
from evmstore.routes.index import bp as index_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(index_bp)

    return app
