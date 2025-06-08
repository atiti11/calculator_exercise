def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("parameter 'b' cannot be 0")
    return a / b


def input_float(prompt):
    while True:
        try:
            inp = input(prompt)
            return float(inp)
        except:
            print("Invalid input. Please enter a valid number.")


def user_add():
    print("You have chosen addition (1st number + 2nd number)")
    num1 = input_float("Enter the first number: ")
    num2 = input_float("Enter the second number: ")
    result = add(num1, num2)
    print(f"Result: {result}")


def user_substract():
    print("You have chosen substraction (1st number - 2nd number)")
    num1 = input_float("Enter the first number: ")
    num2 = input_float("Enter the second number: ")
    result = subtract(num1, num2)
    print(f"Result: {result}")


def user_multiply():
    print("You have chosen multiplication (1st number * 2nd number)")
    num1 = input_float("Enter the first number: ")
    num2 = input_float("Enter the second number: ")
    result = multiply(num1, num2)
    print(f"Result: {result}")


def user_divide():
    print("You have chosen division (1st number / 2nd number)")
    num1 = input_float("Enter the first number: ")
    num2 = input_float("Enter the second number: ")

    try:
        result = divide(num1, num2)
        print(f"Result: {result}")
    except ValueError:
        print("Second number cannot be 0.")


def get_choice():
    print("\nChoose an operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

    choice = input("Enter your choice: ")
    return choice


def main():
    while True:
        choice = get_choice()
        if choice == "0":
            print("Goodbye!")
            break

        if choice == "1":
            user_add()
        elif choice == "2":
            user_substract()
        elif choice == "3":
            user_multiply()
        elif choice == "4":
            user_divide()
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
