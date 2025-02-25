Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... # Task 1
...... uppercase_set = {word.upper() for word in words}
... print(uppercase_set) words = ["hello", "world", "python", "programming"]

... 
... # Task 2
... random_numbers = {random.randint(15, 45) for _ in range(10)}
... count_less_than_30 = sum(1 for num in random_numbers if num < 30)
... random_numbers = {num for num in random_numbers if num <= 35}
... print(random_numbers, count_less_than_30)
... 
... # Task 3
... names_set = set()
... names_set.update(["Alice", "Bob", "Charlie", "David", "Eve"])
... names_set.discard("Bob")
... names_set.discard("Eve")
... names_set.add("Brian")
... print(names_set)
... 
... # Task 4
... names = {"Alice", "Ava", "Aaron", "Bob", "Bill", "Ben"}
... a_names = {name for name in names if name.startswith("A")}
... b_names = {name for name in names if name.startswith("B")}
