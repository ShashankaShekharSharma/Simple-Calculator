import math
import csv
import os

history_file = "calculator_history.csv"


def save_to_csv(operation, result):
    with open(history_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([operation, result])


def load_from_csv():
    if os.path.exists(history_file):
        with open(history_file, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print("No history found.")


def add_numbers(result):
    if result_flag:
        operation = str(result) + "+"
        temp = []
        print(f"Adding numbers to : {result}")
        count = int(input("How many numbers do you want to add? "))
        for i in range(count):
            num = float(input("Enter the number: "))
            result += num
            temp.append(num)
        for i in range(len(temp)):
            if i != len(temp) - 1:
                operation += str(temp[i])
                operation += "+"
            else:
                operation += str(temp[i])
                operation += "="
        print(f"Sum: {result}")
        save_to_csv(operation, result)
        return result

    else:
        num1 = float(input("Enter number 1 : "))
        num2 = float(input("Enter number 2 : "))
        result = num1 + num2
        operation = str(num1) + "+" + str(num2)
        save_to_csv(operation, result)
        print(f"Sum : {result}")
        return result


def subtract_numbers(result):
    if result_flag:
        operation = str(result) + "-"
        temp = []
        print(f"Adding numbers to : {result}")
        count = int(input("How many numbers do you want to subtract? "))
        for i in range(count):
            num = float(input("Enter the number: "))
            result -= num
            temp.append(num)
        for i in range(len(temp)):
            if i != len(temp) - 1:
                operation += str(temp[i])
                operation += "-"
            else:
                operation += str(temp[i])
                operation += "="
        print(f"Sum: {result}")
        save_to_csv(operation, result)
        return result
    else:
        operation = " "
        n1 = float(input("Enter number to subtract from : "))
        n2 = float(input("Enter number to subtract "))
        result = n1 - n2
        operation = str(n1) + "-" + str(n2)
        print(f"Difference : {result}")
        save_to_csv(operation, result)
        return result


def multiply_numbers(result):
    if result_flag:
        operation = str(result) + "*"
        temp = []
        print(f"Adding numbers to : {result}")
        count = int(input("How many numbers do you want to multiply? "))
        for i in range(count):
            num = float(input("Enter the number: "))
            result *= num
            temp.append(num)
        for i in range(len(temp)):
            if i != len(temp) - 1:
                operation += str(temp[i])
                operation += "*"
            else:
                operation += str(temp[i])
                operation += "="
        print(f"Sum: {result}")
        save_to_csv(operation, result)
        return result
    else:
        n1 = float(input("Enter number 1 : "))
        n2 = float(input("Enter number 2 : "))
        result = n1 * n2
        operation = str(n1) + "x" + str(n2)
        print(f"Product : {result}")
        save_to_csv(operation, result)
        return result


def factorial_of_number(result):
    operation = ""
    temp = []
    num = int(input("Enter number to factorial : "))
    fact = 1
    for i in range(1, num + 1):
        temp.append(i)
        fact *= i
    print(f"Factorial: {fact}")
    for i in range(len(temp)):
        if i < (len(temp)-1):
            operation += str(temp[i])
            operation += "x"
        else:
            operation += str(temp[i])
    result = fact
    save_to_csv(operation, result)
    return result


def divide_numbers(result):
    if result_flag:
        print(f"Dividing from(dividend) : {result}")
        num = float(input("Enter the number to divide: "))
        result1 = result
        if num == 0:
            print("Error: Division by zero")
            return result
        result /= num
        operation = str(result) + "/" + str(num)
        print(f"Quotient: {result}")
        save_to_csv(operation, result)
        return result
    else:
        n1 = float(input("Enter dividend : "))
        n2 = float(input("Enter divisor : "))
        result = n1 / n2
        operation = str(n1) + "/" + str(n2)
        print(f"Quotient : {result}")
        save_to_csv(operation, result)
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

        if choice == "13":
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 12:
            print("Invalid choice. Please choose again.")
            continue

        if result_flag:
            radian_val = math.radians(result)
            if choice == "1":
                result=round(math.sin(radian_val),3)
                operations="sine :"+str(radian_val)
            elif choice == "2":
                result=round(math.cos(radian_val),3)
                operations="cosine : "+str(radian_val)
            elif choice == "3":
                result=round(math.tan(radian_val),3)
                operations="tangent : "+str(radian_val)
            elif choice == "4":
                result=round(1/math.cos(radian_val),3)
                operations="secant : "+str(radian_val)
            elif choice == "5":
                result=round(1/math.sin(radian_val),3)
                operations="cosecant : "+str(radian_val)
            elif choice == "6":
                result=round(1/math.tan(radian_val),3)
                operations="cotangent : "+str(radian_val)
            elif choice == "7":
                result=round(math.asin(result),3)
                operations="sine inverse : "+str(radian_val)
            elif choice == "8":
                result=round(math.acos(result),3)
                operations="cosine inverse : "+str(radian_val)
            elif choice == "9":
                result=round(math.atan(result),3)
                operations="tangent inverse : "+str(radian_val)
            elif choice == "10":
                result=round(math.asin(1/result),3)
                operations="cosecant inverse : "+str(radian_val)
            elif choice == "11":
                result=round(math.acos(1/result),3)
                operations="secant inverse : "+str(radian_val)
            elif choice == "12":
                result=round(math.atan(1/result),3)
                operations="cotangent inverse : "+str(radian_val)
            save_to_csv(operations,result)

        else:
            deg = float(input("Enter values in degrees : "))
            radian_val = math.radians(deg)
            if choice == "1":
                result=round(math.sin(radian_val),3)
                operations="sine :"+str(radian_val)
            elif choice == "2":
                result=round(math.cos(radian_val),3)
                operations="cosine : "+str(radian_val)
            elif choice == "3":
                result=round(math.tan(radian_val),3)
                operations="tangent : "+str(radian_val)
            elif choice == "4":
                result=round(1/math.cos(radian_val),3)
                operations="secant : "+str(radian_val)
            elif choice == "5":
                result=round(1/math.sin(radian_val),3)
                operations="cosecant : "+str(radian_val)
            elif choice == "6":
                result=round(1/math.tan(radian_val),3)
                operations="cotangent : "+str(radian_val)
            elif choice == "7":
                result=round(math.asin(result),3)
                operations="sine inverse : "+str(radian_val)
            elif choice == "8":
                result=round(math.acos(result),3)
                operations="cosine inverse : "+str(radian_val)
            elif choice == "9":
                result=round(math.atan(result),3)
                operations="tangent inverse : "+str(radian_val)
            elif choice == "10":
                result=round(math.asin(1/result),3)
                operations="cosecant inverse : "+str(radian_val)
            elif choice == "11":
                result=round(math.acos(1/result),3)
                operations="secant inverse : "+str(radian_val)
            elif choice == "12":
                result=round(math.atan(1/result),3)
                operations="cotangent inverse : "+str(radian_val)
            save_to_csv(operations,result)
        return result


print("Hi! I can perform simple calculations. I can add, multiply, and subtract.")

result_flag = False
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

        if choice == "7":
            print("Exiting the calculator. Goodbye!")
            exit(0)

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 7:
            print("Invalid choice. Please choose again.")
            continue

        if choice == "1":
            result = add_numbers(result)
        elif choice == "2":
            result = subtract_numbers(result)
        elif choice == "3":
            result = multiply_numbers(result)
        elif choice == "4":
            result = divide_numbers(result)
        elif choice == "5":
            result = trigonometric_submenu(result)
        elif choice == "6":
            result = factorial_of_number(result)
        elif choice == "history":
            load_from_csv()
            continue

        choice = input(
            "Do you want to perform another operation on this result? (yes/no): "
        )
        if choice.lower() == "history":
            print("Displaying history:")
            load_from_csv()
            continue
        elif choice.lower() != "yes":
            result = 0

            break
        else:
            result_flag = True
            continue
    choice = input("Do you want to start a new operation? (yes/no): ")
    if choice.lower() != "yes":
        print("Exiting the calculator. Goodbye!")
        break
