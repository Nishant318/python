import random
random_numbers = {random.randint(15, 45) for _ in range(10)}
count_less_than_30 = sum(1 for num in random_numbers if num < 30)
random_numbers = {num for num in random_numbers if num <= 35}
print(random_numbers, count_less_than_30)
