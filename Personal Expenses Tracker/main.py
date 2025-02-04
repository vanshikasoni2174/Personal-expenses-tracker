# main.py
import os
from utils import read_expenses, save_expenses
from expense import Expense

def display_expenses(expenses):
    print("\n----- All Expenses -----")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense.description} - ${expense.amount:.2f} ({expense.category})")
    print()

def add_expense(expenses):
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    expenses.append(Expense(description, amount, category))

def delete_expense(expenses):
    display_expenses(expenses)
    index = int(input("Enter the number of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        expenses.pop(index)
        print("Expense deleted successfully.")
    else:
        print("Invalid index.")

def view_total(expenses):
    total = sum(expense.amount for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}\n")

def export_to_csv(expenses):
    save_expenses("data/expenses.csv", expenses)
    print("\nExpenses have been saved to 'expenses.csv'.")

def main():
    expenses_file = "data/expenses.csv"
    expenses = read_expenses(expenses_file)

    while True:
        print("----- Personal Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. View Total Expense")
        print("5. Export to CSV")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            view_total(expenses)
        elif choice == '5':
            export_to_csv(expenses)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)  # Create data directory if it doesn't exist
    main()
