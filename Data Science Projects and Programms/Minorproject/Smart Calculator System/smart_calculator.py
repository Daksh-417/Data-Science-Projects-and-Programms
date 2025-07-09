import json
import os
from datetime import datetime

HISTORY_FILE = "calc_history.json"

# Save operation result to file
def save_history(entry):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []
    history.append(entry)
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file, indent=4)

# Perform the calculation
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid Operation"

# Main calculator loop
def calculator():
    print("\n📱 Smart Python Calculator - Minor Project")
    while True:
        print("\nAvailable operations:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("🔢 Choose operation (1-5): ")

        if choice == '5':
            print("🛑 Exiting calculator. All operations saved in 'calc_history.json'.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid choice. Please select 1–5.")
            continue

        operator_map = {'1': '+', '2': '-', '3': '*', '4': '/'}
        operator = operator_map[choice]

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid number. Please enter valid numeric input.")
            continue

        result = calculate(num1, num2, operator)

        print(f"✅ Result: {num1} {operator} {num2} = {result}")

        # Save to file
        history_entry = {
            "Operation": f"{num1} {operator} {num2}",
            "Result": result,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_history(history_entry)

# Run the calculator
calculator()
