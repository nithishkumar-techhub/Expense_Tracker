import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add expense/income
def add_entry(data):
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    entry_type = input("Type (income/expense): ").lower()
    date = datetime.now().strftime("%Y-%m-%d")

    entry = {
        "amount": amount,
        "category": category,
        "type": entry_type,
        "date": date
    }

    data.append(entry)
    save_data(data)
    print("✅ Entry added!")

# View all entries
def view_entries(data):
    if not data:
        print("No records found.")
        return

    print("\n📊 All Records:")
    for i, entry in enumerate(data):
        print(f"{i+1}. {entry['date']} | {entry['type']} | {entry['category']} | ₹{entry['amount']}")

# Monthly summary
def monthly_summary(data):
    month = input("Enter month (YYYY-MM): ")
    income = 0
    expense = 0

    for entry in data:
        if entry["date"].startswith(month):
            if entry["type"] == "income":
                income += entry["amount"]
            else:
                expense += entry["amount"]

    print(f"\n📅 Summary for {month}")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Balance: ₹{income - expense}")

# Main menu
def main():
    data = load_data()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_entry(data)
        elif choice == "2":
            view_entries(data)
        elif choice == "3":
            monthly_summary(data)
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()