from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from server.routes.user import user
from server.routes.products import product
from server.routes.api import api
from server.Test.test import test
from .models import db, Product, User

# Data for local database server
DB_NAME = "3162"
DB_URL = f'mysql://ydin0039:StevenDing0039@localhost/{DB_NAME}'

# Data for remote Heroku clearDB server
REMOTE_DB_URL = "mysql://b7a9fd2de96090:7dd6df63@us-cdbr-east-05.cleardb.net/heroku_3e5d99b2aad0cd1"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = REMOTE_DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(test, url_prefix='/test')
    db.init_app(app)
    app.app_context().push()

    @app.route('/')
    def main():
        return render_template('index.html')

    return app



