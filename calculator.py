def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # TODO 2: implementujte tuto funkci podobně jako funkce okolo
    pass


def divide(a, b):
    # TODO 6: do této funkce přidejte kontrolu, že se parametr 'b'
    # nerovná nule -> pokud by se nule rovnal, pak vyhoďte podmnku
    # ValueError("parameter 'b' cannot be zero")
    return a / b


def input_float(prompt):
    # TODO 8: tady chceme, aby uživatel zadal nějaké číslo (může být i desetinné)
    # upravte tuto funkci tak, aby pokud uživatel nezadá číslo (funkce float() vyhodí výjimku),
    # tak vypíšete "Invalid input. Please enter a valid number." a následně se mu
    # znovu dáte možnost napsat nové číslo
    # TIP: použijte nějaký z cyklů
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
    # TODO 5: implementeujte tuto funkci stejně jako jsou
    # implementovány user_add() a user_substract
    pass


def user_divide():
    print("You have chosen division (1st number / 2nd number)")
    num1 = input_float("Enter the first number: ")
    num2 = input_float("Enter the second number: ")

    # TODO 7: spouštění funkce divide obalte blokem try - except
    # pokud funkce divide vyhodí výjimku ValueError, zachyťte ji
    # a vypište "Second number cannot be 0."
    result = divide(num1, num2)
    print(f"Result: {result}")


def get_choice():
    # TODO 1: do console vytiskněte následující řádky:
    # "\nChoose an operation:"
    # "1 - Add"
    # "2 - Subtract"
    # "3 - Multiply"
    # "4 - Divide"
    # "0 - Exit"

    choice = input("Enter your choice: ")
    return choice


def main():
    # TODO 4: všechny operace v této funkci obalte do
    # while loopu, který bude přerušen, pokud uživatel zvolí "0"
    choice = get_choice()
    if choice == "0":
        print("Goodbye!")
    elif choice == "1":
        user_add()
    elif choice == "2":
        user_substract()
    elif choice == "3":
        user_multiply()
    elif choice == "4":
        user_divide()
    else:
        print("Invalid choice. Please select a valid option.")


# TODO 3: spuštění funkce main obalte podmínkou __name__ == "__main__"
main()
