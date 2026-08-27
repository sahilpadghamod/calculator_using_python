def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error! Division by zero is not allowed.")
    return x / y

def main():
    print("--- Command-Line Calculator ---")
    print("Type 'q' to quit or 'c' to clear and start a new calculation.")

    current_value = None

    while True:

        if current_value is None:
            try:
                current_value = float(input("\nEnter the first number: "))
            except ValueError:
                print("Invalid input! Please enter a valid numeric value.")
                continue

        choice = input(f"\n[Current value: {current_value}] Enter operator (+, -, *, /), 'c' to clear, or 'q' to quit: ").strip().lower()

        if choice in ('q', 'quit', 'exit'):
            print("Exiting calcutator. Goodbye!")
            break
        elif choice == 'c':
            print("Cleared!")
            current_value = None
            continue

        if choice in ('+', '-', '*', '/'):
            try:
                next_num = float(input("Enter the second number: "))

                if choice == '+':
                        result = add(current_value, next_num)
                elif choice == '-':
                    result = subtract(current_value, next_num)
                elif choice == '*':
                    result = multiply(current_value, next_num)
                elif choice == '/':
                    result = divide(current_value, next_num)

                print(f"Result: {current_value} {choice} {next_num} = {result}")
                current_value = result
            except ValueError:
                print("Invalid Input! Please enter valid numeric values.")
            except ZeroDivisionError as e:
                print(e)

        else:
            print("Invalid selection! Please choose a valid operator (+, -, *, /) or 'c' to clear and 'q' to quit")

if __name__ == "__main__":
    main()
