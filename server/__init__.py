from flask import Flask, render_template, Blueprint
from server.database import db_session, init_db


def main():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    api = Blueprint('api', __name__)
    app.register_blueprint(api, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    init_db()
    app.run(debug=True)

