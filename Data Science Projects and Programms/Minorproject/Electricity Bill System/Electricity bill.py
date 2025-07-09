import json
import os
from datetime import datetime

BILL_FILE = "bills.json"

def calculate_bill(units):
    if units <= 50:
        bill = units * 2
    elif units <= 100:
        bill = (50 * 2) + (units - 50) * 3
    else:
        bill = (50 * 2) + (50 * 3) + (units - 100) * 5

    tax = bill * 0.05  # 5% GST
    total = bill + tax
    return round(bill, 2), round(tax, 2), round(total, 2)

def save_bill(data):
    all_bills = []

    if os.path.exists(BILL_FILE):
        with open(BILL_FILE, "r") as file:
            try:
                all_bills = json.load(file)
            except json.JSONDecodeError:
                all_bills = []

    all_bills.append(data)

    with open(BILL_FILE, "w") as file:
        json.dump(all_bills, file, indent=4)

def generate_bill():
    print("\n💡 Electricity Bill Generator")
    name = input("👤 Enter Customer Name: ")
    meter_no = input("🔢 Enter Meter Number: ")
    month = input("📅 Enter Billing Month (e.g., July 2025): ")
    
    try:
        units = int(input("⚡ Enter units consumed: "))
        if units < 0:
            print("❌ Units cannot be negative.")
            return
    except ValueError:
        print("❌ Invalid units. Must be a number.")
        return

    base, tax, total = calculate_bill(units)

    bill_data = {
        "Customer Name": name,
        "Meter Number": meter_no,
        "Billing Month": month,
        "Units Consumed": units,
        "Base Bill": base,
        "Tax (5%)": tax,
        "Total Bill": total,
        "Generated At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("\n🧾 Bill Summary:")
    for key, value in bill_data.items():
        if isinstance(value, float):
            print(f"{key}: ₹{value}")
        else:
            print(f"{key}: {value}")

    save_bill(bill_data)
    print("✅ Bill saved successfully.\n")

def main():
    while True:
        generate_bill()
        more = input("➕ Do you want to add another customer? (y/n): ").lower()
        if more != 'y':
            print("📁 All bills saved in 'bills.json'. Exiting.")
            break

main()
