from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from server.routes.api import api

app = Flask(__name__)
REMOTE_DB_URL = "mysql://b7a9fd2de96090:7dd6df63@us-cdbr-east-05.cleardb.net/heroku_3e5d99b2aad0cd1"
app.config['SQLALCHEMY_DATABASE_URI'] = REMOTE_DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_size": 20}
app.register_blueprint(api, url_prefix='/api')
db = SQLAlchemy(app)
db.create_all()
engine = db.create_engine(REMOTE_DB_URL)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


@app.route('/')
def main():
    return render_template('index.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run()

