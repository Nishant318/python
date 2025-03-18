# 6. Recursive function to sanitize list by replacing negatives with 0
def sanitize_list(lst, i=0):
    if i == len(lst):
        return lst
    if lst[i] < 0:
        lst[i] = 0
    return sanitize_list(lst, i + 1)

lst = [-1, 2, -3, 4, -5]
sanitize_list(lst)
print(lst)  # Example call
