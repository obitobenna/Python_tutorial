def calculate_area(base, height):
    try:
        base = float(base)
        height = float(height)
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative.")
        return 0.5 * base * height
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An error occurred: ", str(e))

base = input("Please enter the base of the triangle: ")
height = input("Please enter the height of the triangle: ")

area = calculate_area(base, height)
if area is not None:
    print("The area of the triangle is: ", area)
else:
    print("Invalid input. Please enter numeric values for base and height.")