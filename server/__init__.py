from flask import Flask, render_template, Blueprint
from server.database import db_session, init_db
from server.routes.api import api


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable the event notification system since we don't need it
    # and disable it for saving system resources

    app.register_blueprint(api, url_prefix='/api')   # Register a blueprint on an application at a URL prefix '/api/'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    init_db()

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
