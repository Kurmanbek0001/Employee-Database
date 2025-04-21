from employee import Employee
from employee_dao import EmployeeDAO

def main():
    dao = EmployeeDAO()

    # Insert
    new_emp = Employee(None, "Kurmanbek", "Software Developer", 70000, "2025-04-21")
    dao.insert(new_emp)
    print("Inserted new employee.")

    # Get all
    print("\nAll Employees:")
    for emp in dao.get_all():
        print(emp)

    # Get by ID
    print("\nEmployee with ID 1:")
    emp = dao.get_by_id(1)
    print(emp if emp else "Not found")

    # Update
    if emp:
        emp.salary = 80000
        dao.update(emp)
        print("\nUpdated Employee:")
        print(dao.get_by_id(1))

    # Delete
    dao.delete(1)
    print("\nAfter Deletion:")
    for emp in dao.get_all():
        print(emp)

if __name__ == "__main__":
    main()

