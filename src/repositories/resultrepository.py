from connect_db import get_db_connection
class ResultRepository():
    def __init__(self, connection):
        self._connection = connection

    def save_info(self, username, timer):
        cursor = self._connection.cursor()
        sql = 'INSERT INTO results (username, timer) VALUES (:username, :timer)'
        cursor.execute(sql, {"username" : username, "timer" : timer})
        self._connection.commit()
    
    def get_scoreboard(self):
        cursor = self._connection.cursor()
        sql = 'SELECT * FROM results ORDER BY timer'
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    
    def delete_all(self):
        cursor = self._connection.cursor()
        sql = 'DELETE FROM results'
        cursor.execute(sql)
        self._connection.commit()
    
