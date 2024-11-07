# initialize_db.py
from dao.database_connection import DatabaseConnection

def initialize_db():
    conn = DatabaseConnection.get_instance()
    cursor = conn.cursor()
    
    # Create employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            salary REAL,
            hours_per_week REAL
        )
    ''')
