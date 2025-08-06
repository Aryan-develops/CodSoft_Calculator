import sys

def get_number(prompt):
    """Prompt user for a number, repeat until valid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def display_menu():
    print("\n=== Unique Calculator ===")
    print("Welcome to your personalized Python calculator!")
    print("Select an operation:")
    print(" 1. Add")
    print(" 2. Subtract")
    print(" 3. Multiply")
    print(" 4. Divide")
    print(" 5. Exit")

def perform_calculation(choice, a, b):
    if choice == '1':
        return f"{a} + {b} = {a + b}"
    elif choice == '2':
        return f"{a} - {b} = {a - b}"
    elif choice == '3':
        return f"{a} * {b} = {a * b}"
    elif choice == '4':
        if b == 0:
            return "Error: You can't divide by zero!"
        return f"{a} / {b} = {a / b}"

def main():
    print("Welcome to the Unique Python Calculator!")
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '5':
            print("Thank you for using the Unique Calculator. Goodbye!")
            sys.exit()
        elif choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            result = perform_calculation(choice, num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid choice, please pick a valid option.")

if __name__ == "__main__":
    main()