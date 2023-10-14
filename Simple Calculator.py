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
    
def factorial_of_number(result):
    num = int(input("Enter number to factorial : "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial: {fact}")
    result=fact
    return result

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
        n2=float(input("Enter divisor : "))
        result=n1/n2
        print(f"Quotient : {result}")
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
        
        if result_flag:
            radian_val = math.radians(result)
            if choice == '1':
                print(f"Sine value: {round(math.sin(radian_val),3)}")
            elif choice == '2':
                print(f"Cosine value: {round(math.cos(radian_val),3)}")
            elif choice == '3':
                print(f"Tangent value: {round(math.tan(radian_val),3)}")
            elif choice == '4':
                print(f"Secant value: {round(1/math.cos(radian_val),3)}")
            elif choice == '5':
                print(f"Cosecant value: {round(1/math.sin(radian_val),3)}")
            elif choice == '6':
                print(f"Cotangent value: {round(1/math.tan(radian_val),3)}")
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
                
        else:
            deg=float(input("Enter values in degrees : "))
            radian_val=math.radians(deg)
            if choice == '1':
                print(f"Sine value: {round(math.sin(radian_val),3)}")
            elif choice == '2':
                print(f"Cosine value: {round(math.cos(radian_val),3)}")
            elif choice == '3':
                print(f"Tangent value: {round(math.tan(radian_val),3)}")
            elif choice == '4':
                print(f"Secant value: {round(1/math.cos(radian_val),3)}")
            elif choice == '5':
                print(f"Cosecant value: {round(1/math.sin(radian_val),3)}")
            elif choice == '6':
                print(f"Cotangent value: {round(1/math.tan(radian_val),3)}")
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
        print("4. Division")
        print("5. Trigonometric submenu")
        print("6. Factorial")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            exit(0)

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 7:
            print("Invalid choice. Please choose again.")
            continue

        if choice == '1':
            result = add_numbers(result)
        elif choice == '2':
            result = subtract_numbers(result)
        elif choice == '3':
            result = multiply_numbers(result)
        elif choice=='4':
            divide_numbers(result)
        elif choice == '5':
            trigonometric_submenu(result)
        elif choice =='6':
            factorial_of_number(result)

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
