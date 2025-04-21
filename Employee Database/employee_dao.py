import sqlite3
from employee import Employee

class EmployeeDAO:
    def __init__(self):
        self.conn = sqlite3.connect('employee_db.sqlite')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                position TEXT,
                salary REAL,
                hire_date TEXT
            )
        ''')
        self.conn.commit()

    def insert(self, employee):
        self.cursor.execute('''
            INSERT INTO employee (name, position, salary, hire_date)
            VALUES (?, ?, ?, ?)
        ''', (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM employee WHERE id = ?", (id,))
        row = self.cursor.fetchone()
        return Employee(*row) if row else None

    def get_all(self):
        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()
        return [Employee(*row) for row in rows]

    def update(self, employee):
        self.cursor.execute('''
            UPDATE employee
            SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?
        ''', (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM employee WHERE id = ?", (id,))
        self.conn.commit()
