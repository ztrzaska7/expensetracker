class Expense:
    def __init__(self,date,amount,notes,category):
        self.date=date
        self.amount=amount
        self.notes=notes
        self.category=category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    def add_expense(self,date,amount,notes,category):
        expense=Expense(amount,date,notes,category)
        self.expenses.append(expense)
    def get_total_expenses(self):
        total=0
        for expense in self.expenses:
            total += expense.amount
        return total
    def get_expense_category(self,category):
        category_expense=[]
        for expense in self.expenses:
            if expense.category == category:
                category_expense.append(expense)
        return category_expense

tracker = ExpenseTracker()
tracker.add_expense(10.50, "2023-05-01", "Jedzenie", "Obiad w restauracji")
tracker.add_expense(25.00, "2023-05-02", "Transport", "Bilet autobusowy")
tracker.add_expense(15.75, "2023-05-03", "Rozrywka", "Bilet do kina")
total_expenses = tracker.get_total_expenses()
print(f"total expenses: {total_expenses}")

food_expenses=tracker.get_expense_category("Jedzenie")
print("Expenses for food is:")
for expense in food_expenses:
    print(f"Amount: {expense.amount},category: {expense.category}, notes: {expense.notes}")
