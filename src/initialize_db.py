from connect_db import get_db_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS results;
    ''')
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE results (
            username TEXT, 
            timer TIME
        );
    ''')
    connection.commit()

def initialize_db():
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_db()