# Personal-expenses-tracker
Overview
The Personal Expense Tracker is a simple Python application designed to help users track their expenses. It allows users to:

Add, view, and delete expenses.
Categorize each expense.
View the total expenses.
Export expense data to a CSV file for future reference or analysis.
This project is aimed at helping individuals manage their personal finances by providing an easy-to-use interface for tracking and analyzing their spending.

Features
Add Expense: Add an expense with a description, amount, and category.
View Expenses: View all recorded expenses in a list format.
Delete Expense: Delete an expense by selecting its number from the list.
View Total Expenses: See the total amount spent across all categories.
Export to CSV: Export your expenses to a CSV file for further analysis or record-keeping.
Technologies Used
Python: The project is built using Python, utilizing basic file operations and user input for functionality.
CSV: Expenses are stored and managed in a CSV file for simplicity and easy access.
No external dependencies: This project does not require any third-party libraries.
How to Run the Project
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/your-username/expense-tracker.git
Navigate to the project directory:

bash
Copy
Edit
cd expense-tracker
Run the main Python script:

bash
Copy
Edit
python main.py
Follow the interactive prompts in the terminal to add, view, delete expenses, or export data.

Usage Example
After running the program, you'll be presented with a menu. Here’s an example of how the interaction might look like:

pgsql
Copy
Edit
----- Personal Expense Tracker -----
1. Add Expense
2. View Expenses
3. Delete Expense
4. View Total Expense
5. Export to CSV
6. Exit
Choose an option: 1
Enter the description of the expense: Coffee
Enter the amount: 5.50
Enter the category: Food

----- Personal Expense Tracker -----
1. Add Expense
2. View Expenses
3. Delete Expense
4. View Total Expense
5. Export to CSV
6. Exit
Choose an option: 2

----- All Expenses -----
1. Coffee - $5.50 (Food)

How to Contribute
If you’d like to contribute to this project:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to your forked repository (git push origin feature-branch).
Submit a pull request with a description of your changes.
