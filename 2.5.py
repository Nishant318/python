def check_age_status(age):
    if age < 18:
        return "Minor"
    else:
        return "Major"

age = int(input("Enter the age of the person: "))

status = check_age_status(age)

print(f"The person is a {status}.")
