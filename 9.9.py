# 9. Function to count uppercase and lowercase alphabets and digits
def count_alpha_digits(s):
    result = {"alphabets": sum(c.isalpha() for c in s), "digits": sum(c.isdigit() for c in s)}
    return result

# Sample test
print(count_alpha_digits("Hello123"))
