from flask import Flask, render_template
from server.database import db_session, init_db, drop_db
from server.db_script import insert_products
from server.routes.api import api
from server.routes.admin import admin


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable the event notification system since we don't need it
    SECRET_KEY = b'\xed\xeeM\xaaK\r\xc0@xw@\xb6\xd0 S9[z\xde$\xc6\x9a\x13}\xa3\xfa\xdb[\xb1\x98\x08\xa9'
    app.config['SECRET_KEY'] = SECRET_KEY

    # It uses blueprints to allow us to separate various endpoints into subdomains. Here we define the prefix of all
    # API endpoints registered with the blueprint to be “api” and therefore our base API endpoint is “/api”
    app.register_blueprint(api, url_prefix='/api')  # Register a blueprint on an application at a URL prefix '/api/'

    app.register_blueprint(admin, url_prefix='/admin')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    # uncomment to drop all the db tables
    # drop_db()

    # initialises any db tables that didn't already exist
    init_db()

    # uncomment to populate product data from json (after drop_db)
    # insert_products()

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
