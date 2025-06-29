import sqlite3
import pandas as pd

class DBConnector:
    def __init__(self, db_path : str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
    def run_query(self, sql_query : str) -> pd.DataFrame:
        cursor = (self.conn).cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        result_pd = pd.DataFrame(result)
        return result_pd
    def close(self):
        if(self.conn):
            self.conn.close()
            self.conn = None
    def is_closed(self) -> bool:
        return self.conn is None

