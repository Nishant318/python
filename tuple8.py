employees = [
    (101, 'Amit', 35, 'HR', 10000),
    (102, 'Rahul', 40, 'IT', 20000),
    (103, 'Priya', 30, 'Finance', 25000),
    (104, 'Anita', 28, 'HR', 15000),
    (105, 'Vikram', 38, 'IT', 30000)
]

departments = (
    ('HR', 'Human Resources', 'Building A'),
    ('IT', 'Information Technology', 'Building B'),
    ('Finance', 'Financial Services', 'Building C')
)

def filter_by_department(dept):
    return [emp[1] for emp in employees if emp[3] == dept]

def sort_by_salary():
    return sorted(employees, key=lambda x: x[4])

def highest_salary():
    return max(employees, key=lambda x: x[4])

def update_salary(emp_id, new_salary):
    global employees
    employees = [(id, name, age, dept, new_salary if id == emp_id else salary) for id, name, age, dept, salary in employees]

nested_departments = {dept[0]: (dept[1], dept[2]) for dept in departments}

print(filter_by_department('HR'))
print(sort_by_salary())
print(highest_salary())
update_salary(101, 12000)
print(employees)
print(nested_departments)
