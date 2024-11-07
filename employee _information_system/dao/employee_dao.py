# dao/employee_dao.py
from dao.database_connection import DatabaseConnection
from models.employee_types import FullTimeEmployee, PartTimeEmployee, ContractEmployee

class EmployeeDAO:
    def __init__(self):
        self.conn = DatabaseConnection.get_instance()

    def add_employee(self, employee):
        cursor = self.conn.cursor()
        emp_type = employee.get_employee_type()
        try:
            if isinstance(employee, PartTimeEmployee):
                cursor.execute(
                    'INSERT INTO employees (name, type, salary, hours_per_week) VALUES (?, ?, ?, ?)',
                    (employee.name, emp_type, employee.salary, employee.hours_per_week)
                )
            else:
                cursor.execute(
                    'INSERT INTO employees (name, type, salary) VALUES (?, ?, ?)',
                    (employee.name, emp_type, employee.salary)
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
            if emp_type == "Part-Time Employee":
                return PartTimeEmployee(name, salary, hours)
            elif emp_type == "Full-Time Employee":
                return FullTimeEmployee(name, salary)
            elif emp_type == "Contract Employee":
                return ContractEmployee(name, salary)
        return None

