# 4. Function to calculate total and average marks
def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average
marks= input()
print(sum_avg)
