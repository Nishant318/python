# 8. Function to return a sorted unique string
def convert(s):
    return "".join(sorted(set(s.replace(" ", ""))))

# Sample test
print(convert("hello world"))
