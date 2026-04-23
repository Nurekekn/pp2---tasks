import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="zamanbek",
        password="Zama123"
    )