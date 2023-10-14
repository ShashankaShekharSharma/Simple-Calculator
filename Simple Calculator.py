import math
def add_numbers(result):
    if result_flag:
        print(f"Adding numbers to : {result}")
        count = int(input("How many numbers do you want to add? "))
        for i in range(count):
            num = float(input("Enter the number: "))
            result += num
        print(f"Sum: {result}")
        return result
    else:
        num1=float(input("Enter number 1 : "))
        num2=float(input("Enter number 2 : "))
        result=num1+num2
        print(f"Sum : {result}")
        return result

def subtract_numbers(result):
    if result_flag:
        print(f"Subtratcting from {result}")
        num = float(input("Enter the number to subtract: "))
        result -= num
        print(f"Difference: {result}")
        return result
    else:
        n1=float(input("Enter number to subtract from : "))
        n2=float(input("Enter number to subtract "))
        result=n1-n2
        print(f"Difference : {result}")
        return result

def multiply_numbers(result):
    if result_flag:
        print(f"Multiplying to : {result}")
        num = float(input("Enter the number to multiply: "))
        result *= num
        print(f"Product: {result}")
        return result
    else:
        n1=float(input("Enter number 1 : "))
        n2=float(input("Enter number 2 : "))
        result=n1*n2
        print(f"Product : {result}")
        return result
      
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
            print(f"Sine inverse value: {round(math.degrees(math.asin(result)),2)}")
        elif choice == '8':
            print(f"Cosine inverse value: {round(math.degrees(math.acos(result)),2)}")
        elif choice == '9':
            print(f"Tangent inverse value: {round(math.degrees(math.atan(result)),2)}")
        elif choice == '10':
            print(f"Cosecant inverse value: {round(math.degrees(math.asin(1/result)),2)}")
        elif choice == '11':
            print(f"Secant inverse value: {round(math.degrees(math.acos(1/result)),2)}")
        elif choice == '12':
            print(f"Cotangent inverse value: {round(math.degrees(math.atan(1/result)),2}")

def divide_numbers(result):
    if result_flag:
        print(f"Dividing from(dividend) : {result}")
        num = float(input("Enter the number to divide: "))
        if num == 0:
            print("Error: Division by zero")
            return result
        result /= num
        print(f"Quotient: {result}")
        return result
    else:
        n1=float(input("Enter dividend : "))
        n2=float(input("Enter divisor "))
        result=n1/n2
        print(f"Quotient : {result}")
        return result

print("Hi! I can perform simple calculations. I can add, multiply, and subtract.")

result_flag=False
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
            result_flag=True
            continue
    choice = input("Do you want to start a new operation? (yes/no): ")
    if choice.lower() != 'yes':
        print("Exiting the calculator. Goodbye!")
        break
