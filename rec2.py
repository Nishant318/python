# 2. Recursive function to find binary equivalent of a number
def binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary(n // 2) + str(n % 2)

print(binary(10))  
