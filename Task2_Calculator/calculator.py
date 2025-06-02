#Task 2 : Simple Calculator
# Author: Dharmesh J
# Date : 03.06.25

#Step 1: Input two numbers
#Step 2: Show operations (+,-,*,/)
#Step 3: Get user choice
#Step 4: Perform the operation and display the result
def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2
def choose_operation():
    print("Please select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice
def calculate(num1, num2, operator):
    if operator == '1':
        return num1 + num2
    elif operator == '2':
        return num1 - num2
    elif operator == '3':
        return num1 * num2
    elif operator == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation selected."
# Main program execution
while True:
    print("\n🧮 Welcome to Simple Calculator")

    num1, num2 = get_numbers()
    operator = choose_operation()
    result = calculate(num1, num2, operator)
    
    print(f"🧾 Result: {result}")

    # Ask user if they want to calculate again
    again = input("\nDo you want to perform another calculation? (y/n): ").lower()
    if again != 'y':
        print("👋 Thank you for using the calculator. Goodbye!")
        break
