# expense.py

class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f"Expense(description={self.description}, amount={self.amount}, category={self.category})"
