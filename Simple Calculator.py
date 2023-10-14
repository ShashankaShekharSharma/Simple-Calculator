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


print("Hi! I can perform simple calculations. I can add, multiply, and subtract.")

result = 0
while True:
    while True:
        print("\nChoose the operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '4':
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
