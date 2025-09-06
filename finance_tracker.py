import json
from decimal import Decimal

# file where data will be stored
DATA_FILE = "transactions.json"

# -------------------------------
# helpers to load/save data
# -------------------------------
def load_data():
    """load transactions if file exists, else return empty list"""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(transactions):
    """save transactions into the json file"""
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)

# -------------------------------
# input helpers
# -------------------------------
def read_amount(msg):
    """read a decimal number from user safely"""
    while True:
        raw = input(msg).strip()
        try:
            amt = Decimal(raw)
            if amt < 0:
                print("amount can’t be negative.")
                continue
            return amt
        except:
            print("please enter a valid number (e.g. 123.45)")

# -------------------------------
# core stuff
# -------------------------------
def get_balance(transactions):
    """calculate current balance"""
    income = sum(Decimal(t["amount"]) for t in transactions if t["type"] == "Income")
    expense = sum(Decimal(t["amount"]) for t in transactions if t["type"] == "Expense")
    return income - expense

def add_transaction(transactions, kind):
    """add an income or expense"""
    amount = read_amount(f"enter {kind.lower()} amount: ")

    # stop expense if not enough money
    if kind == "Expense":
        bal = get_balance(transactions)
        if amount > bal:
            print(f"not enough balance. you only have {bal:.2f}.")
            return

    valid_categories = ["Salary", "Food", "Rent"]
    category = input("category (Salary, Food, Rent): ").strip().title()
    if category not in valid_categories:
        category = "Uncategorized"

    transactions.append({"type": kind, "amount": str(amount), "category": category})
    print(f"{kind} of {amount:.2f} added under '{category}'")

def show_balance(transactions):
    """print income, expense, balance"""
    income = sum(Decimal(t["amount"]) for t in transactions if t["type"] == "Income")
    expense = sum(Decimal(t["amount"]) for t in transactions if t["type"] == "Expense")
    bal = income - expense

    print("\nBalance Report:")
    print(f"  Income : {income:.2f}")
    print(f"  Expense: {expense:.2f}")
    print(f"  Balance: {bal:.2f}")

def show_transactions(transactions):
    """print all transactions"""
    if not transactions:
        print("no transactions yet.")
        return
    print("\nTransaction History:")
    for i, t in enumerate(transactions, start=1):
        print(f"{i:02d}. {t['type']:<7} {Decimal(t['amount']):>10.2f}  ({t['category']})")

def expense_summary(transactions):
    """group expenses by category"""
    if not transactions:
        print("no transactions to summarize.")
        return
    cats = {}
    for t in transactions:
        if t["type"] == "Expense":
            cats[t["category"]] = cats.get(t["category"], Decimal("0")) + Decimal(t["amount"])
    print("\nExpense Summary:")
    for cat, amt in cats.items():
        print(f"- {cat:<15} {amt:.2f}")

def delete_transaction(transactions):
    """delete one transaction"""
    if not transactions:
        print("nothing to delete.")
        return
    show_transactions(transactions)
    try:
        choice = int(input("\nenter transaction number to delete: "))
        if 1 <= choice <= len(transactions):
            removed = transactions.pop(choice - 1)
            print(f"deleted: {removed['type']} {removed['amount']} ({removed['category']})")
        else:
            print("invalid number.")
    except ValueError:
        print("please enter a number.")

def delete_all(transactions):
    """delete all transactions if user confirms"""
    if not transactions:
        print("nothing to delete.")
        return
    confirm = input("delete ALL transactions? (yes/no): ").strip().lower()
    if confirm == "yes":
        transactions.clear()
        save_data(transactions)
        print("all transactions deleted.")
    else:
        print("cancelled.")

# -------------------------------
# main loop
# -------------------------------
def main():
    print("=== Personal Finance Tracker ===")
    transactions = load_data()

    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Transactions")
        print("5. Expense Summary")
        print("6. Delete Transaction")
        print("7. Delete ALL Transactions")
        print("8. Exit & Save")

        choice = input("choose: ").strip()

        if choice == "1":
            add_transaction(transactions, "Income")
        elif choice == "2":
            add_transaction(transactions, "Expense")
        elif choice == "3":
            show_balance(transactions)
        elif choice == "4":
            show_transactions(transactions)
        elif choice == "5":
            expense_summary(transactions)
        elif choice == "6":
            delete_transaction(transactions)
        elif choice == "7":
            delete_all(transactions)
        elif choice == "8":
            save_data(transactions)
            print("saved. bye!")
            break
        else:
            print("invalid option.")

if __name__ == "__main__":
    main()
