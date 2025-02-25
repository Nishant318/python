employees = {'HR': [(101, 50000), (102, 60000)], 'IT': [(103, 70000), (104, 80000)]}
for dept, data in employees.items():
    salaries = [sal for _, sal in data]
    print(f"{dept}: Min={min(salaries)}, Max={max(salaries)}")
