import json
import os
import datetime

ACCOUNT_FILE = "account.json"

def setup_account():
    if not os.path.exists(ACCOUNT_FILE):
        print("\n🆕 No account found. Let's create one.")
        pin = input("🔑 Set a 4-digit PIN: ")
        while not (pin.isdigit() and len(pin) == 4):
            pin = input("❌ Invalid PIN. Enter a 4-digit PIN: ")

        balance = input("💰 Enter initial deposit amount: ₹")
        while not balance.isdigit():
            balance = input("❌ Please enter a valid amount: ₹")

        data = {
            "pin": pin,
            "balance": int(balance),
            "history": [
                {"type": "Deposit", "amount": int(balance), "time": timestamp()}
            ]
        }

        with open(ACCOUNT_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print("✅ Account created successfully!\n")

def load_account():
    with open(ACCOUNT_FILE, 'r') as f:
        return json.load(f)

def save_account(data):
    with open(ACCOUNT_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def insert_card():
    card = input("🪪 Insert your card (type 'card' to insert): ").strip().lower()
    return card == "card"

def verify_pin(saved_pin):
    for attempt in range(3):
        pin = input("🔑 Enter your 4-digit PIN: ")
        if pin == saved_pin:
            return True
        else:
            print("❌ Incorrect PIN.")
    print("🚫 Too many incorrect attempts. Card retained.")
    return False

def show_menu():
    print("\n🧾 MENU:")
    print("1️⃣  Check Balance")
    print("2️⃣  Withdraw Money")
    print("3️⃣  Deposit Money")
    print("4️⃣  View Transaction History")
    print("5️⃣  Exit")

def atm_interface():
    print("\n🏦 Welcome to KotaK ATM 🏦")
    if not insert_card():
        print("❌ No card detected.")
        return

    account = load_account()

    if not verify_pin(account["pin"]):
        return

    while True:
        show_menu()
        choice = input("👉 Choose an option (1–5): ")

        if choice == "1":
            print(f"💰 Your current balance is: ₹{account['balance']}")

        elif choice == "2":
            amount = input("💸 Enter amount to withdraw: ₹")
            if not amount.isdigit():
                print("❌ Invalid input.")
                continue
            amount = int(amount)
            if amount > account["balance"]:
                print("⚠️ Insufficient balance.")
            else:
                account["balance"] -= amount
                account["history"].append({
                    "type": "Withdraw",
                    "amount": amount,
                    "time": timestamp()
                })
                save_account(account)
                print(f"✅ Withdrawn ₹{amount}. Remaining balance: ₹{account['balance']}")

        elif choice == "3":
            amount = input("💵 Enter amount to deposit: ₹")
            if not amount.isdigit():
                print("❌ Invalid input.")
                continue
            amount = int(amount)
            account["balance"] += amount
            account["history"].append({
                "type": "Deposit",
                "amount": amount,
                "time": timestamp()
            })
            save_account(account)
            print(f"✅ Deposited ₹{amount}. New balance: ₹{account['balance']}")

        elif choice == "4":
            print("\n📜 Transaction History:")
            for txn in account["history"][-10:]:  # Show last 10 transactions
                print(f"{txn['time']} - {txn['type']} ₹{txn['amount']}")

        elif choice == "5":
            print("🔒 Transaction ended. Please take your card.")
            break

        else:
            print("❌ Invalid option. Please try again.")

# First-time setup (if file doesn't exist)
setup_account()

# Start ATM system
atm_interface()
