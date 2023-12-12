import os
import sqlite3
from config import DATABASE_FILENAME_PATH

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(DATABASE_FILENAME_PATH)
connection.row_factory = sqlite3.Row

def get_db_connection():
    return connection