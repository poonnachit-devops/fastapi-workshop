from pydantic import BaseModel
from datetime import datetime

class Expenses(BaseModel):
    id: int
    description: str
    amount: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class ExpensesDto(BaseModel):
    id: int
    description: str
    amount: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

expenses: dict[int,Expenses] = {}
id = 0

def add_expense_tracker(description: str, amount: int) -> None:
    global id
    id += 1

    expenses[id] = Expenses(id=id, description=description, amount=amount)
    
    print(f"expense added successfully ({id}, {description}, {amount} baht)")

def update_expense_tracker(id: int, description: str, amount: int) -> None:
    if id not in expenses:
        print(f"expense with id {id} not found")
        return
    
    global expenses
    expenses[id] = Expenses(id=id, description=description, amount=amount, updated_at=datetime.now())
    print(f"expense updated successfully ({id}, {description}, {amount} baht)")

def delete_expense_tracker(id: int) -> None:
    global expenses
    if id not in expenses:
        print(f"expense with id {id} not found")
        return
    del expenses[id]

def list_expense_tracker() -> None:
    print("ID\tDate\t\tDescription\tAmount")
    for _, expense in expenses.items():
        print(f"{expense.id}\t{expense.created_at.date()}\t{expense.description}\t{expense.amount} baht")

def summary_expense_tracker(month: int | None = None) -> None:
    if not month:
        total = sum(expense.amount for expense in expenses.values())
        print(f"Total expenses: {total} baht")
        return
    total = sum(expense.amount for expense in expenses.values() if expense.created_at.month == month)
    print(f"Total expenses for month {get_month_name(month)}: {total} baht")

def get_month_name(month: int) -> str:
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return month_names[month - 1] if 1 <= month <= 12 else "Invalid month"


add_expense_tracker("Water", 10)
add_expense_tracker("Coke", 15)
add_expense_tracker("Green tea", 15)

update_expense_tracker(1, "Water", 8)

delete_expense_tracker(3)

summary_expense_tracker()
summary_expense_tracker(6)
