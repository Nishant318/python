# 8. Recursive function to obtain length of a string
def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])

print(string_length("Hello"))  # Example call
