# Configurações do banco de dados
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "desafio_engenheiro",
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def close_db_connection(connection):
    connection.close()

def get_cursor(connection):
    return connection.cursor()

def close_cursor(cursor):
    cursor.close()

def execute_query(cursor, query, params=None):
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

def fetch_data(cursor, query, params=None):
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    return cursor.fetchall()
