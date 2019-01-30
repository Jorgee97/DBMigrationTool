from sqlalchemy import create_engine
from .constants import ENGINES


class EngineDetails(object):
    def __init__(self, driver, username, password, host, database):
        self.driver = driver
        self.username = username
        self.password = password
        self.host = host
        self.database = database


class ConnectEngine(object):
    def __init__(self, engine_name, **engine_parameters):
        """
        This class will create a connection to a database engine, using SqlAlchemy create_engine
        :param engine_name: This is the engine that we want to connect to. (i.e: mssql, mysql, postgres)
        :param engine_parameters: This is the dictionary that contains the database, user, password and host
        """
        self.engine_connection = None
        for engine in ENGINES:
            if engine_name in engine:
                self.eng_connection(engine[engine_name], engine_parameters)

    def eng_connection(self, eng, eng_params):
        self.engine_connection = \
            create_engine(f"{eng['driver']}://{eng_params['username']}:{eng_params['password']}@{eng_params['host']}/"
                          f"{eng_params['database']}")

    def get_engine_connection(self):
        return self.engine_connection


def validate_sql_statement(query):
    if query[-2] == ',':
        return query[:-2] + ')'
    return query

