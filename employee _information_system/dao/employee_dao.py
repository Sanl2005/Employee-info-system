# dao/employee_dao.py
import sqlite3
from database_connection import DatabaseConnection
from models.employee_types import FullTimeEmployee, PartTimeEmployee, ContractEmployee

class EmployeeDAO:
    def __init__(self):
        self.conn = DatabaseConnection.get_instance()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        """Create the employees table if it doesn't already exist."""
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                salary REAL NOT NULL,
                hours_per_week INTEGER
            )
            ''')
            self.conn.commit()
        except sqlite3.DatabaseError as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()

    def add_employee(self, employee):
        cursor = self.conn.cursor()
        try:
            if isinstance(employee, PartTimeEmployee):
                cursor.execute(
                    'INSERT INTO employees (name, type, salary, hours_per_week) VALUES (?, ?, ?, ?)',
                    (employee.name, employee.type, employee.salary, employee.hours_per_week)
                )
            else:
                cursor.execute(
                    'INSERT INTO employees (name, type, salary) VALUES (?, ?, ?)',
                    (employee.name, employee.type, employee.salary)
                )
            self.conn.commit()
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()

    def get_employee(self, emp_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM employees WHERE id = ?', (emp_id,))
        result = cursor.fetchone()
        cursor.close()
        
        if result:
            emp_type, name, salary, hours = result[2], result[1], result[3], result[4]
            if emp_type == "Part-Time":
                return PartTimeEmployee(name, salary, hours)
            elif emp_type == "Full-Time":
                return FullTimeEmployee(name, salary)
            elif emp_type == "Contract":
                return ContractEmployee(name, salary)
        return None

    def get_all_employees(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM employees')
        employees = cursor.fetchall()
        cursor.close()
        return employees

    def delete_employee(self, emp_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
        self.conn.commit()
        cursor.close()
