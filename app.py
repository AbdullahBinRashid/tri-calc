import math


is_angle_type_correct = False
is_angle_correct = False


while not is_angle_type_correct:
    angle_type = input("Which type of angle do you want to work with?\n(d for Degree or r for Radian): ").lower()

    if angle_type == "r":
        is_angle_type_correct = True
    elif angle_type == "d":
        is_angle_type_correct = True
    else:
        print("Wrong angle type!")

while not is_angle_correct:
    try:
        angle_in_radian = float(input("Enter angle: "))
        is_angle_correct = True
    except ValueError:
        print("Invalid Angle!")


if angle_type == "r":
    angle = angle_in_radian
elif angle_type == "d":
    angle = angle_in_radian * math.pi / 180





is_function_correct = False

while not is_function_correct:
    function = input("Enter function: ").lower()

    if function == "sin" or function == "s":
        result = math.sin(angle)
        is_function_correct = True
    elif function == "cos" or function == "c":
        result = math.cos(angle)
        is_function_correct = True
    elif function == "tan" or function == "t":
        result = math.tan(angle)
        is_function_correct = True
    else:
        print("Invalid trigonometric function!")


if is_function_correct and is_angle_type_correct:
    print(f"Your answer = {result}")

input("Enter any key to continue!")
