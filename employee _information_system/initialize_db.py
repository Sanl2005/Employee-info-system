import sqlite3
import os

# Define the path to the database file
db_folder = "E:\employee _information_system\employee_management_system"
db_file = os.path.join(db_folder, "employee_database.db")

# Check if the database folder exists; if not, create it
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

# Connect to SQLite (creates the file if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create an example table for employees
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        salary REAL NOT NULL,
        hours_per_week REAL  -- This column is optional for Part-Time employees
    )
''')

# Commit and close
conn.commit()
conn.close()

print(f"Database '{db_file}' created successfully with the employees table.")
