# 1. Recursive function to obtain prime factors of a number
def prime_factors(n, i=2):
    if i>n:
        return None
    if n % i == 0:
        return prime_factors(n // i, i)
    return prime_factors(n, i + 1)
num=int(input("enter any number"))

print(prime_factors(56)) 
