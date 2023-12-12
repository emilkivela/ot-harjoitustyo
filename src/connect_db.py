import os
import sqlite3
from config import DATABASE_FILENAME

connection = sqlite3.connect(DATABASE_FILENAME)
connection.row_factory = sqlite3.Row

def get_db_connection():
    return connection