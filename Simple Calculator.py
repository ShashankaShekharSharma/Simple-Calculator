import math
import csv
import os
import time
import numpy as np
import matplotlib.pyplot as plt
start_time = time.time()
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

def solve_quadratic_equation(result):
    print("Enter the coefficients of the quadratic equation (ax^2 + bx + c = 0):")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discriminant = b * b - 4 * a * c
    operation = 'Solving the equation: '+str(a)+'x^2'+str(b)+'x+'+str(c)+'=0'
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The roots are real and distinct: {root1} and {root2}")
        ans=[root1,root2]
    elif discriminant == 0:
        root1 = root2 = -b / (2 * a)
        print(f"The roots are real and equal: {root1} and {root2}")
        ans=[root1,root2]
    else:
        realPart = -b / (2 * a)
        imaginaryPart = math.sqrt(-discriminant) / (2 * a)
        print(f"The roots are complex and different: {realPart}+{imaginaryPart}i and {realPart}-{imaginaryPart}i")
        ans = [str(realPart)+'i'+str(imaginaryPart)+'j',str(realPart)+'i-'+str(imaginaryPart)+'j']
    save_to_csv(operation, ans)

def solve_cubic_equation(result):
    print("Enter the coefficients of the cubic equation (ax^3 + bx^2 + cx + d = 0):")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))
    operation = 'Solving the equation: ' + str(a) + 'x^3' + str(b) + 'x^2+' + str(c)+'x+'+str(d) + '=0'
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)

    discriminant = q ** 2 / 4 + p ** 3 / 27
    if discriminant > 0:
        S = (q / 2 + math.sqrt(discriminant)) ** (1 / 3)
        T = (q / 2 - math.sqrt(discriminant)) ** (1 / 3)
        root1 = -b / (3 * a) - (S + T)
        print(f"The real root is: {root1}")
        imaginary = (S - T) * math.sqrt(3) / 2
        root2 = -b / (3 * a) + (S + T) / 2 + imaginary
        root3 = -b / (3 * a) + (S + T) / 2 - imaginary
        print(f"The complex roots are: {root2} and {root3}")
        ans=[str(root1),str(root2)+'j'+str(root3)+'j']
        save_to_csv(operation,ans)
    elif discriminant == 0:
        if q < 0:
            A = (abs(q) / 2) ** (1 / 3)
            root1 = -b / (3 * a) - 2 * A
            root2 = -b / (3 * a) + A
            print(f"The real root is: {root1} and the complex root is: {root2} + {root2}i")
            ans=[str(root1),str(root2)+'i'+str(root2)+'j']
            save_to_csv(operation,ans)
        else:
            A = (-q / 2) ** (1 / 3)
            root1 = -b / (3 * a) - 2 * A
            root2 = -b / (3 * a) + A
            print(f"The real root is: {root1} and the complex root is: {root2} - {root2}i")
            ans=[str(root1),str(root2)+'i-'+str(root2)+'j']
            save_to_csv(operation,ans)
    else:
        x = math.sqrt((q ** 2 / 4) - discriminant)
        θ = math.acos(-q / (2 * math.sqrt(discriminant)))
        root1 = 2 * math.sqrt(-p / 3) * math.cos(θ / 3) - b / (3 * a)
        root2 = 2 * math.sqrt(-p / 3) * math.cos((θ + 2 * math.pi) / 3) - b / (3 * a)
        root3 = 2 * math.sqrt(-p / 3) * math.cos((θ + 4 * math.pi) / 3) - b / (3 * a)
        print(f"The roots are: {root1}, {root2}, and {root3}")
        ans=[root1,root2,root3]
        save_to_csv(operation,ans)

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


def polynomial_graph(result):
    degree = int(input("Enter the degree of the polynomial: "))
    coefficients = []
    for i in range(degree + 1):
        coefficient = float(input(f"Enter the coefficient for x^{i}: "))
        coefficients.append(coefficient)
    y = 0
    for i in range(len(coefficients)):
        y += coefficients[i] * x**i
    return y
    x = np.linspace(-10, 10, 400)
    y = polynomial(x, coefficients)
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Polynomial Equation', color='b')
    plt.title('Graph of the Polynomial Equation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid()
    plt.show()
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

def log(result):
    if result_flag:
        print("taking log of ",result)
        num = input("Enter the base: (type 'e' for natural log)")
        num = int(num)
        if num == 'e':
            result = math.log(result)
            print(result)
        elif num > 0:
            result = math.log(result,num)
            print(result)
        else:
            result("invalid")
        operation = 'log of'+str(result)+'base'+str(num)
        save_to_csv(operation,result)
    else:
        a = int(input("enter the number "))
        num = int(input("Enter the base "))
        if a>0 and num>0:
            result=math.log(a,num)
            operation='log of '+str(a)+ 'base'+ str(num)
            save_to_csv(operation,result)
            print(result)
        else:
            print("invalid")
def plot_polynomial(degree, coefficients):
    # Function to evaluate the polynomial equation
    def polynomial(x, coefficients):
        y = 0
        for i in range(len(coefficients)):
            y += coefficients[i] * x**i
        return y

    # Generate x values
    x = np.linspace(-10, 10, 400)

    # Compute corresponding y values
    y = polynomial(x, coefficients)

    # Plot the graph
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Polynomial Equation', color='b')
    plt.title('Graph of the Polynomial Equation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid()
    plt.show()
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
        print("Type history to see previous calculations")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Trigonometric submenu")
        print("6. Factorial")
        print("7. Solve Quadratic Equation")
        print("8. Solve Cubic Equations")
        print("9. Logarithms")
        print("10. Graph of Polynomial Equation")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "11":
            print("Exiting the calculator. Goodbye!")
            end_time = time.time()
            time_spent = end_time - start_time
            print("Time spent on Calculator = "+str(round(time_spent,2))+"s")
            exit(0)

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 11:
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
        elif choice == "7":
            result = solve_quadratic_equation(result)
        elif choice == "8":
            result = solve_cubic_equation(result)
        elif choice == "9":
            result = log(result)
        elif choice == "10":
            degree = int(input("Enter the degree of the polynomial: "))
            coefficients = []
            for i in range(1,degree + 1):
                coefficient = float(input(f"Enter the coefficient for x^{i}: "))
                coefficients.append(coefficient)
            const=int(input("Enter the value of constant term "))
            coefficients.append(const)
            plot_polynomial(degree, coefficients)
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
        end_time = time.time()
        time_spent = end_time - start_time
        print("Time spent on Calculator = " + str(round(time_spent, 2)) + "s")
        break
