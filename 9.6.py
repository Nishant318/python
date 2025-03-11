# 6. Function to return tuples (x, x²) from 1 to n
def create_tuples(n):
    return [(x, x ** 2) for x in range(1, n + 1)]

# Sample test
print(create_tuples(5))
