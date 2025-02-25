def separate_pos_neg():
    numbers = [random.randint(-50, 50) for _ in range(30)]
    positive = [num for num in numbers if num > 0]
    negative = [num for num in numbers if num < 0]

    print(f"Original List: {numbers}")
    print(f"Positive Numbers: {positive}")
    print(f"Negative Numbers: {negative}")
