def calculate_total_and_average(sub1, sub2, sub3):
    total = sub1 + sub2 + sub3  
    average = total / 3    
    print(f"Marks in Subject 1: {sub1}")
    print(f"Marks in Subject 2: {sub2}")
    print(f"Marks in Subject 3: {sub3}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

calculate_total_and_average(sub1, sub2, sub3)
