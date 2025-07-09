import json
import os
from datetime import datetime

TICKET_FILE = "tickets.json"
BASE_PRICE = 100  # Base price for a regular adult ticket

def calculate_fare(age, quantity):
    if age < 5:
        fare = 0
        category = "Child (Free)"
    elif age <= 12:
        fare = BASE_PRICE * 0.75  # 25% discount
        category = "Child"
    elif age >= 60:
        fare = BASE_PRICE * 0.85  # 15% discount
        category = "Senior Citizen"
    else:
        fare = BASE_PRICE
        category = "Adult"

    total_fare = round(fare * quantity, 2)
    return total_fare, category, fare

def save_ticket(data):
    tickets = []
    if os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, "r") as file:
            try:
                tickets = json.load(file)
            except json.JSONDecodeError:
                tickets = []

    tickets.append(data)
    with open(TICKET_FILE, "w") as file:
        json.dump(tickets, file, indent=4)

def book_ticket():
    print("\n🎟️ Welcome to Dynamic Ticket Booking System")
    name = input("👤 Enter your name: ")
    try:
        age = int(input("🎂 Enter your age: "))
        quantity = int(input("🔢 Number of tickets to book: "))
        if age < 0 or quantity <= 0:
            print("❌ Invalid input. Age and quantity must be positive.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    total_price, category, unit_price = calculate_fare(age, quantity)

    ticket_data = {
        "Name": name,
        "Age": age,
        "Category": category,
        "Unit Ticket Price": unit_price,
        "Quantity": quantity,
        "Total Price": total_price,
        "Booking Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("\n🧾 Ticket Summary:")
    for key, value in ticket_data.items():
        print(f"{key}: ₹{value}" if isinstance(value, (int, float)) else f"{key}: {value}")

    save_ticket(ticket_data)
    print("✅ Ticket booked and saved successfully.\n")

def main():
    while True:
        book_ticket()
        again = input("➕ Book another ticket? (y/n): ").lower()
        if again != 'y':
            print("📁 All bookings saved in 'tickets.json'. Thank you!")
            break

main()
