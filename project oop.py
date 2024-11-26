import csv


class Employee:
    def __init__(self, emp_id, name, department, role):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.role = role

class EmployeeManager:
    def __init__(self, filename='employees.csv'):
        self.filename = filename
        self.load_employees()

    def load_employees(self):
        self.employees = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                
                required_columns = ['ID', 'Name', 'Department', 'Role']
                if not all(col in reader.fieldnames for col in required_columns):
                    print(f"CSV file is missing one or more required columns: {required_columns}")
                    return
                
                for row in reader:
                    self.employees.append(Employee(row['ID'], row['Name'], row['Department'], row['Role']))
        except FileNotFoundError:
            
            with open(self.filename, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Department', 'Role'])
                writer.writeheader()

    def save_employees(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Department', 'Role'])
            writer.writeheader()
            for emp in self.employees:
                writer.writerow({'ID': emp.emp_id, 'Name': emp.name, 'Department': emp.department, 'Role': emp.role})

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        role = input("Enter Role: ")
        self.employees.append(Employee(emp_id, name, department, role))
        print("Employee added successfully!")

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
            else
        print("Employee List:")
        for emp in self.employees:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Department: {emp.department}, Role: {emp.role}")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.name = input(f"Enter new name (current: {emp.name}): ") or emp.name
                emp.department = input(f"Enter new department (current: {emp.department}): ") or emp.department
                emp.role = input(f"Enter new role (current: {emp.role}): ") or emp.role
                print("Employee updated successfully!")
                else
        print("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print("Employee deleted successfully!")
                else
        print("Employee not found.")

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print(f"ID: {emp.emp_id}, Name: {emp.name}, Department: {emp.department}, Role: {emp.role}")
                else
        print("Employee not found.")


def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Data Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.view_employees()
        elif choice == '3':
            manager.update_employee()
        elif choice == '4':
            manager.delete_employee()
        elif choice == '5':
            manager.search_employee()
        elif choice == '6':
            manager.save_employees()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

