# 2. Function to compute n + nn + nnn + nnnn
def compute(n):
     return n + int(str(n) * 2) + int(str(n) * 3) + int(str(n) * 4)
