 # 1. Function to count uppercase and lowercase letters in a string
def count_lower_upper(s):
     count = {"uppercase": 0, "lowercase": 0}
     for char in s:
         if char.isupper():
             count["uppercase"] += 1
         elif char.islower():
             count["lowercase"] += 1
     return count
