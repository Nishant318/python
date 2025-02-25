def find_largest_smallest(a, b, c):
    largest = max(a, b, c)
    smallest = min(a, b, c)
    return largest, smallest

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest, smallest = find_largest_smallest(num1, num2, num3)

print(f"The largest value is: {largest}")
print(f"The smallest value is: {smallest}")
