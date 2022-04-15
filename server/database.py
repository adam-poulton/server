from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


REMOTE_DB_URL = "mysql://b7a9fd2de96090:7dd6df63@us-cdbr-east-05.cleardb.net/heroku_3e5d99b2aad0cd1"

engine = create_engine(REMOTE_DB_URL, pool_pre_ping=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import server.models
    Base.metadata.create_all(bind=engine)


def drop_db():
    import server.models
    Base.metadata.drop_all(bind=engine)
