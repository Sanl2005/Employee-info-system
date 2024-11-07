# dao/database_connection.py
import sqlite3

class DatabaseConnection:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnection._instance is None:
            DatabaseConnection._instance = sqlite3.connect('employee.db')
        return DatabaseConnection._instance

