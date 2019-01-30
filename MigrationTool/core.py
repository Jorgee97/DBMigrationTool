from sqlalchemy import inspect
from .helpers import ConnectEngine
from .mssql_to_postgresql import create_tables, migrate_data_to_postgres, migrate_constraints
from .constants import MSSQL_TO_POSTGRESQL, MIGRATE_ALL, MIGRATE_TABLES_VIEW, MIGRATE_TABLES_DATA, MIGRATE_TABLES


def mssql_postgresql(mssql_details, postgres_details, option, app):
    eng_mssql = ConnectEngine(
        mssql_details.driver,
        database=mssql_details.database,
        username=mssql_details.username,
        password=mssql_details.password,
        host=mssql_details.host).get_engine_connection()

    eng_postgresql = ConnectEngine(
        postgres_details.driver,
        database=postgres_details.database,
        username=postgres_details.username,
        password=postgres_details.password,
        host=postgres_details.host).get_engine_connection()

    insp_mssql = inspect(eng_mssql)
    insp_postgresql = inspect(eng_postgresql)

    table_names_mssql = insp_mssql.get_table_names()
    table_names_postgresql = insp_postgresql.get_table_names()
    table_names = list(set(table_names_mssql) - set(table_names_postgresql))

    if option == MIGRATE_ALL:
        create_tables(table_names, insp_mssql, eng_postgresql)
        migrate_data_to_postgres(table_names_mssql, eng_mssql, eng_postgresql)
        migrate_constraints(table_names_mssql, insp_mssql, insp_postgresql, eng_postgresql)
    elif option == MIGRATE_TABLES_DATA:
        create_tables(table_names, insp_mssql, eng_postgresql)
        migrate_data_to_postgres(table_names_mssql, eng_mssql, eng_postgresql)
        migrate_constraints(table_names_mssql, insp_mssql, insp_postgresql, eng_postgresql)
    elif option == MIGRATE_TABLES:
        create_tables(table_names, insp_mssql, eng_postgresql)
        migrate_constraints(table_names_mssql, insp_mssql, insp_postgresql, eng_postgresql)
    elif option == MIGRATE_TABLES_VIEW:
        app.warningBox("Error", "This option has not been implemented yet. Sorry for the inconvenience")


def migrate_database(target, actual_db_details, target_db_details, option, app):
    if target == MSSQL_TO_POSTGRESQL:
        mssql_postgresql(actual_db_details, target_db_details, option, app)










