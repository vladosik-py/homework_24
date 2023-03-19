from flask import Flask

import config
from views import main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(main_bp)
    return app