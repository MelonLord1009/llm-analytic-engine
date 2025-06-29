import pytest
from src.query_engine.db_connector import DBConnector

def test_db_connection():
    db_path = "path"
    connection = DBConnector(db_path)
    assert connection.db_path == db_path
    connection.close()
    assert connection.is_closed
 


