"""A simple command-line calculator."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Simple Calculator")
    first = get_number("First number: ")
    operator = input("Operator (+, -, *, /): ").strip()
    second = get_number("Second number: ")

    operations = {
        "+": lambda: first + second,
        "-": lambda: first - second,
        "*": lambda: first * second,
        "/": lambda: first / second,
    }
    if operator not in operations:
        print("Unsupported operator.")
    elif operator == "/" and second == 0:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {operations[operator]():g}")


if __name__ == "__main__":
    main()
