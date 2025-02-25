def swap (a,b):
    a,b = b,a
    print(a,b)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("After swap: ")
print(swap(x,y))
