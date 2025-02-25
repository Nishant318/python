def find_largest_smallest(a, b):
    largest = max(a, b)
    smallest = min(a, b)
    return largest, smallest

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

largest, smallest = find_largest_smallest(num1, num2)

print(f"The largest value is: {largest}")
print(f"The smallest value is: {smallest}")
