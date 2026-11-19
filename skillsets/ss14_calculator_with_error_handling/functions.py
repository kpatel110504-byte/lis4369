
"""functions.py file for main"""


def get_requirements():
    """Prints program requirements."""
    print("Developer: Khushi Patel")
    print("Python Calculator with Error Handling")

    print("\nProgram Requirements:\n"
          + "1. Program calculates two numbers and rounds to two decimal places.\n"
          + "2. Prompt user for two numbers and a suitable operator.\n"
          + "3. Use Python error handling to validate data.\n"
          + "4. Test for correct arithmetic operator.\n"
          + "5. Division by zero is not permitted.\n"
          + "6. Program loops until correct input is entered.\n"
          + "7. Supports addition, subtraction, multiplication, division,\n"
          + "   integer division, modulo, and power.")


def get_valid_float(pos):
    """Gets and validates a number from the user."""
    while True:
        try:
            num = float(input("\nEnter num" + str(pos) + ": "))
            return num

        except ValueError:
            print("Not valid number! Please try again.")


def get_valid_operator():
    """Gets and validates an arithmetic operator."""
    print("\nSuitable Operators: +, -, *, /, //, %, **")

    op_list = ['+', '-', '*', '/', '//', '%', '**']

    while True:
        op_test = input("Enter operator: ")

        if op_test in op_list:
            return op_test

        else:
            print("Incorrect operator! Please try again.")


def error_handling():
    """Performs calculations with error handling."""

    # Get valid inputs
    num1 = get_valid_float(1)
    num2 = get_valid_float(2)
    op = get_valid_operator()

    # Perform calculation
    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2

    elif op == "/":
        while True:
            try:
                result = num1 / num2
                break

            except ZeroDivisionError:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)

    elif op == "//":
        while True:
            try:
                result = num1 // num2
                break

            except ZeroDivisionError:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)

    elif op == "%":
        while True:
            try:
                result = num1 % num2
                break

            except ZeroDivisionError:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)

    elif op == "**":
        result = num1 ** num2

    # Display result
    print("{0:,.2f}".format(result))

    print("\nThank you for using our math calculator!")
