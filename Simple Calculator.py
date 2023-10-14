import math
def add_numbers(result):
    count = int(input("How many numbers do you want to add? "))
    for i in range(count):
        num = float(input("Enter the number: "))
        result += num
    print(f"Sum: {result}")
    return result

def subtract_numbers(result):
    print(f"Subtratcting from {result}")
    num = float(input("Enter the number to subtract: "))
    result -= num
    print(f"Difference: {result}")
    return result

def multiply_numbers(result):
    num = float(input("Enter the number to multiply: "))
    result *= num
    print(f"Product: {result}")
    return result
def trigonometric_submenu(result):
    while True:
        print("\nTrigonometric functions:")
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        print("4. Sec")
        print("5. Cosec")
        print("6. Cot")
        print("7. Sin inverse")
        print("8. Cos inverse")
        print("9. Tan inverse")
        print("10. Cosec inverse")
        print("11. Sec inverse")
        print("12. Cot inverse")
        print("13. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '13':
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 12:
            print("Invalid choice. Please choose again.")
            continue
            radian_val = math.radians(result)

        if choice == '1':
            print(f"Sine value: {math.sin(radian_val)}")
        elif choice == '2':
            print(f"Cosine value: {math.cos(radian_val)}")
        elif choice == '3':
            print(f"Tangent value: {math.tan(radian_val)}")
        elif choice == '4':
            print(f"Secant value: {1/math.cos(radian_val)}")
        elif choice == '5':
            print(f"Cosecant value: {1/math.sin(radian_val)}")
        elif choice == '6':
            print(f"Cotangent value: {1/math.tan(radian_val)}")
        elif choice == '7':
            print(f"Sine inverse value: {math.degrees(math.asin(result))}")
        elif choice == '8':
            print(f"Cosine inverse value: {math.degrees(math.acos(result))}")
        elif choice == '9':
            print(f"Tangent inverse value: {math.degrees(math.atan(result))}")
        elif choice == '10':
            print(f"Cosecant inverse value: {math.degrees(math.asin(1/result))}")
        elif choice == '11':
            print(f"Secant inverse value: {math.degrees(math.acos(1/result))}")
        elif choice == '12':
            print(f"Cotangent inverse value: {math.degrees(math.atan(1/result))}")



print("Hi! I can perform simple calculations. I can add, multiply, and subtract.")

result = 0
while True:
    while True:
        print("\nChoose the operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Trigonometric submenu")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            exit(0)

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 3:
            print("Invalid choice. Please choose again.")
            continue

        if choice == '1':
            result = add_numbers(result)
        elif choice == '2':
            result = subtract_numbers(result)
        elif choice == '3':
            result = multiply_numbers(result)
        elif choice == '4':
            trigonometric_submenu(result)


        choice = input("Do you want to perform another operation on this result? (yes/no): ")
        if choice.lower() != 'yes':
            result=0
            break
        else:
            continue
    choice = input("Do you want to start a new operation? (yes/no): ")
    if choice.lower() != 'yes':
        print("Exiting the calculator. Goodbye!")
        break
