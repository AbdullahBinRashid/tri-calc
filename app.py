import math


is_angle_type_correct = False
is_angle_correct = False
angle_in_radian = 0


while not is_angle_type_correct:
    angle_type = input("Which type of angle do you want to work with?\n(d for Degree or r for Radian): ").lower()

    if angle_type == "r":
        angle = angle_in_radian
        is_angle_type_correct = True
    elif angle_type == "d":
        angle = angle_in_radian * 180 / math.pi
        is_angle_type_correct = True
    else:
        print("Wrong angle type!")


while not is_angle_correct:
    try:
        angle_in_radian = float(input("Enter angle: "))
        is_angle_correct = True
    except ValueError:
        print("Invalid Angle!")

is_function_correct = False

while not is_function_correct:
    function = input("Enter function: ").lower()

    if function == "sin":
        result = math.sin(angle)
        is_function_correct = True
    elif function == "cos":
        result = math.cos(angle)
        is_function_correct = True
    elif function == "tan":
        result = math.tan(angle)
        is_function_correct = True
    else:
        print("Invalid trigonometric function!")

if is_function_correct and is_angle_type_correct:
    print(f"Your answer = {result}")

input("Enter any key to continue!")
