# dao/database_connection.py
import sqlite3


class DatabaseConnection:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = sqlite3.connect("employee_database.db", check_same_thread=False)
        return cls._instance


