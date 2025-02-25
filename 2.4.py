def check_divisible_by_10(number):
    if number % 10 == 0:
        return "Divisible by 10"
    else:
        return "Not divisible by 10"

num = int(input("Enter a number: "))

result = check_divisible_by_10(num)

print(f"The number {num} is {result}.")
