# 💰 Personal Finance Tracker

A simple and intuitive **Python CLI tool** to track your income and expenses, helping you manage your personal finances efficiently.

---

## 📌 Features

- **Add Income and Expenses**  
- **View current balance** at any time  
- **Categorized Expense Summary** (Food, Salary, Rent, Uncategorized)  
- **Delete** individual transactions or clear all transactions  
- **Data persistence** using JSON  

---

## 🗂 Project Structure

```text
personal-finance-tracker/
├─ transactions.json       # JSON file storing transaction data
├─ main.py                 # Main Python program
├─ requirements.txt        # Dependencies (if any)
├─ README.md               # Project documentation
└─ .gitignore              # Ignored files (pycache, env, etc.)



---
```

## ⚙️ Installation

1. **Clone the repository**  
```bash
-> git clone https://github.com/<okox01>/personal-finance-tracker.git    
    cd personal-finance-tracker
-> pip install -r requirements.txt
-> python main.py

---
```
```
# 🖥️ How to Use

When you run the program, you’ll see a menu like this:

Menu:
1. Add Income
2. Add Expense
3. Show Balance
4. Show Transactions
5. Expense Summary
6. Delete Transaction
7. Delete ALL Transactions
8. Exit & Save


Select the number corresponding to your choice.

Add amounts, categories, and see your balance update in real-time.

Expenses exceeding your current balance are automatically prevented.

Categories outside Food, Salary, Rent are automatically labeled Uncategorized.
```

# 🔧 Technology Stack

Python 3.x

JSON for data storage

Decimal module for precise financial calculations

# 💡 How It Works

All transactions are stored in transactions.json.

You can add Income or Expense entries, each with a category.

The program calculates your current balance dynamically.

Expense entries cannot exceed the available balance.

Categories outside predefined ones are automatically labeled as Uncategorized.

# 📈 Future Enhancements

Add visual graphs for income vs expenses.

Generate monthly and yearly reports.

Add CSV import/export functionality.

Build a GUI version using Tkinter or PyQt.

# ⚠️ Notes

Ensure Python 3.x is installed on your machine.

The JSON file (transactions.json) is created automatically if it doesn’t exist.

This is a CLI-based project, suitable for learning Python and building a portfolio.


# 📜 License

MIT License © 2025 <MD.Sayed Ahmed Sami>
