ENGINES = [
    {'mssql': {
        'driver': 'mssql+pymssql'
    }},
    {'postgresql': {
        'driver': 'postgresql+psycopg2'
    }}
]

MSSQL_TO_POSTGRESQL = "mssql_postgresql"

# TODO: 1. Give correct transaction types to the available_engines object.
# TODO: 2. Fix the types that are not correct following this table:
#  https://www.convert-in.com/docs/mss2pgs/types-mapping.htm
ENGINES_CONVERSION = [
    {'mssql_postgresql': {
        'NVARCHAR': 'varchar',
        'VARCHAR': 'varchar',
        'NCHAR': 'CHAR',
        'INTEGER': 'int',
        'BINARY': 'bytea',
        'VARBINARY': 'bytea',
        'DATE': 'date',
        'TINYINT': 'int',
        'SMALLINT': 'int',
        'SMALLDATETIME': 'timestamp',
        'MONEY': 'money',
        'SMALLMONEY': 'money',
        'IMAGE': 'bytea',
        'FLOAT': 'float',
        'BIT': 'BOOLEAN',
        'NTEXT': 'text',
        'TEXT': 'text',
        'CHAR': 'char',
        'REAL': 'real',
        'NUMERIC': 'numeric',
        'DECIMAL': 'decimal',
        'TIME': 'time',
        'DATETIME': 'timestamp'}}
]

MIGRATE_TABLES = "Migrate Tables Only"
MIGRATE_TABLES_DATA = "Migrate Tables + Data"
MIGRATE_TABLES_VIEW = "Migrate Tables + Views"
MIGRATE_ALL = "Migrate Tables + Data and Views"
