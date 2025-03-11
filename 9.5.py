# 5. Function to check if a string is a pangram
import string

def ispangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))

# Sample test
print(ispangram("The quick brown fox jumps over the lazy dog"))  # True
print(ispangram("Hello World"))
