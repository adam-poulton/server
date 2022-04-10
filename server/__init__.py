from flask import Flask, render_template, Blueprint
from server.database import db_session, init_db
from server.routes import routes


def main():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    api = Blueprint('api', __name__)
    app.register_blueprint(api, url_prefix='/api')
    product = Blueprint('products', __name__)
    api.register_blueprint(product, url_prefix='/product')
    user = Blueprint('users', __name__)
    api.register_blueprint(user, url_prefix='/user')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    init_db()

    return app


if __name__ == "__main__":
    app.run(debug=True)
