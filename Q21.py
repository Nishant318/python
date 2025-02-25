def calculate_net_salary(gross_salary):
    allowance = 0.10 * gross_salary  
    deduction = 0.03 * gross_salary  
    net_salary = gross_salary + allowance - deduction  
    print(f"Gross Salary: {gross_salary}")
    print(f"Allowance (10%): {allowance}")
    print(f"Deduction (3%): {deduction}")
    print(f"Net Salary: {net_salary}")

gross_salary = float(input("Enter your gross salary: "))
calculate_net_salary(gross_salary)
