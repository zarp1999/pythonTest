import sqlenv
from sqlalchemy import create_engine


def connect_db():
    engine = create_engine("mysql://" + sqlenv.db_user + ":" +
                           sqlenv.db_password + "@" + sqlenv.db_server, echo=True)
    return engine


def create_db(db):
    engine = connect_db()
    engine.execute("CREATE DATABASE IF NOT EXISTS " + db)


def use_db(db):
    engine = connect_db()
    engine.execute("USE " + db)
    return engine
