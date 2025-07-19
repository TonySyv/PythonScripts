import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (e.g., Food, Transport): ").strip()
        date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            date = datetime.today().date()

        expense = {
            "amount": amount,
            "category": category,
            "date": str(date)
        }
        expenses.append(expense)
        print("Expense added!")
    except ValueError:
        print("Invalid input. Please try again.")

def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nExpenses:")
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} - {exp['category']}: ${exp['amount']:.2f}")
        total += exp['amount']
    print(f"\nTotal expenses: ${total:.2f}\n")

def main():
    expenses = load_expenses()

    while True:
        print("Options:")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
