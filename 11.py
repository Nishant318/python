import math
x = float(input("Enter value of x in radians: "))
terms = 10
sin_x = 0
for i in range(terms):
    sign = (-1) ** i
    sin_x += sign * (x ** (2 * i + 1)) / factorial(2 * i + 1)
print("sin(x):", sin_x)
print("Using math.sin:", math.sin(x))
