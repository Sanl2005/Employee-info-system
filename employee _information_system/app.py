from flask import Flask, render_template, request, redirect, url_for, session, flash
from dao.employee_dao import EmployeeDAO
from models.employee_types import FullTimeEmployee, PartTimeEmployee, ContractEmployee

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure key
employee_dao = EmployeeDAO()

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple login validation (replace with a secure authentication mechanism)
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials", "danger")
    return render_template('login.html')

# Route for the dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# Route to add an employee
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        emp_type = request.form['type']
        salary = float(request.form['salary'])
        if emp_type == 'Part-Time':
            hours = float(request.form['hours'])
            employee = PartTimeEmployee(name, salary, hours)
        elif emp_type == 'Full-Time':
            employee = FullTimeEmployee(name, salary)
        elif emp_type == 'Contract':
            employee = ContractEmployee(name, salary)
        employee_dao.add_employee(employee)
        flash("Employee added successfully!", "success")
        return redirect(url_for('dashboard'))
    return render_template('add_employee.html')

# Route to view employees
@app.route('/view')
def view_employee():
    if 'username' not in session:
        return redirect(url_for('login'))
    employees = employee_dao.get_all_employees()
    return render_template('view_employee.html', employees=employees)

# Route to delete an employee
@app.route('/delete/<int:emp_id>', methods=['POST'])
def delete_employee(emp_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    employee_dao.delete_employee(emp_id)
    flash("Employee deleted successfully!", "success")
    return redirect(url_for('view_employee'))

# Route to log out
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
