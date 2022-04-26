from flask import Flask, render_template, Blueprint
from dotenv import load_dotenv
from server.database import db_session, init_db, drop_db
from server.db_script import insert_products
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

    # uncomment to drop all the db tables
    # drop_db()

    # initialises any db tables that aren't already created
    init_db()

    # uncomment to populate product data from json (after drop_db)
    # insert_products()

    return app


if __name__ == "__main__":
    load_dotenv()
    create_app().run(debug=True)
