num = int(input("Enter a number: "))

# Check if the entered number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

age = int(input("Enter your age: "))

# Determine the life stage based on the entered age
if age >= 0 and age <= 12:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
else:
    print("You are an adult")

year = int(input("Enter a year:"))

# Check if the entered year is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

