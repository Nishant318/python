# 7. Recursive function to obtain average of all numbers in a list
def average(lst, i=0, total=0):
    if i == len(lst):
        return total / len(lst) if len(lst) > 0 else 0
    return average(lst, i + 1, total + lst[i])

print(average([1, 2, 3, 4, 5]))  # Example call

