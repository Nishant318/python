# 7. Function to check if a string is a palindrome
def ispalindrome(s):
    s = s.replace(" ", "").lower()  # Removing spaces and converting to lowercase
    return s == s[::-1]

# Sample test
print(ispalindrome("madam"))  # True
print(ispalindrome("hello"))  # False

