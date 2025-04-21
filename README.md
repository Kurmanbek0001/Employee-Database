# Employee Management System (SQLite + Python)

This is a Python-based application that demonstrates how to perform CRUD (Create, Read, Update, Delete) operations on an employee database using SQLite. The project follows an object-oriented approach with two main classes: `Employee` (entity class) and `EmployeeDAO` (data access object).

---

## Features

- Create employee records
- View a specific employee by ID
- View all employee records
- Update existing employee data
- Delete employee by ID
- SQLite used for data persistence

---

## Database Schema

Database: `employee_db.sqlite`  
Table: `employee`

| Column     | Type     | Description                    |
|------------|----------|--------------------------------|
| id         | INTEGER  | Primary Key (Auto Increment)   |
| name       | TEXT     | Employee Name                  |
| position   | TEXT     | Job Position                   |
| salary     | REAL     | Monthly Salary                 |
| hire_date  | TEXT     | Hire Date (YYYY-MM-DD format)  |

---

## File Structure

