# utils.py
import csv
from expense import Expense

def read_expenses(file_path):
    expenses = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                description, amount, category = row
                expenses.append(Expense(description, float(amount), category))
    except FileNotFoundError:
        pass  # File not found, we will create a new one later
    return expenses

def save_expenses(file_path, expenses):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Description", "Amount", "Category"])  # Header
        for expense in expenses:
            writer.writerow([expense.description, expense.amount, expense.category])
