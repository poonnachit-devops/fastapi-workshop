# 🧾 Expense Tracker with Pydantic & Type Hints

In this task, we’ll build a simple **expense tracker** using Python, where we:

- Define a `Pydantic` model to validate expense data.
- Create functions (with type hints!) to manage the tracker: **add**, **update**, **delete**, **view**, and **summarize** expenses.

---

## 🔧 Step 1: Define the Expense Model

We'll start by creating a Pydantic class to validate each expense:

```python
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
```

---

## ➕ Step 2: Add an Expense

Create a function to add a new expense with a description and amount.

- The function should auto-generate the ID.
- After adding, print a confirmation like:

```
expense added successfully (ID, DESCRIPTION, AMOUNT baht)
```

### Example:

```python
add_expense_tracker("Water", 10)
# output: expense added successfully (1, Water, 10 baht)

add_expense_tracker("Coke", 15)
# output: expense added successfully (2, Coke, 15 baht)

add_expense_tracker("Green tea", 15)
# output: expense added successfully (3, Green tea, 15 baht)
```

---

## ✏️ Step 3: Update an Expense by ID

Create a function that updates an expense’s **description and amount** using its ID.

- After updating, print a confirmation like:

```
expense updated successfully (ID, DESCRIPTION, AMOUNT baht)
```

### Example:

```python
update_expense_tracker(1, "Water", 8)
# output: expense updated successfully (1, Water, 8 baht)
```

---

## ❌ Step 4: Delete an Expense

Create a function to delete an expense by ID.

- After deletion, print:

```
DESCRIPTION has been deleted
```

### Example:

```python
delete_expense_tracker(3)
# output: Green tea has been deleted
```

---

## 📄 Step 5: View All Expenses

Create a function to display all expenses in a table format:

```plaintext
ID  Date        Description  Amount
1   2024-08-06  Water        8
2   2024-08-06  Coke         15
```

---

## 💰 Step 6: View Total Summary

Create a function to print the total of all expenses:

```python
summary_expense_tracker()
# output: Total expenses: 23 baht
```

---

## 📆 Step 7: Monthly Summary

Modify the summary function to optionally accept a month (1-12) and show the total for that month (from the current year):

```python
summary_expense_tracker(8)
# output: Total expenses for August: 23 baht
```

---

## ✅ Final Output Example

```python
add_expense_tracker("Water", 10)
add_expense_tracker("Coke", 15)
add_expense_tracker("Green tea", 15)

update_expense_tracker(1, "Water", 8)

delete_expense_tracker(3)

summary_expense_tracker()
summary_expense_tracker(6)
```

### Sample Output:

```
expense added successfully (1, Water, 10 baht)
expense added successfully (2, Coke, 15 baht)
expense added successfully (3, Green tea, 15 baht)
expense updated successfully (1, Water, 8 baht)
Green tea has been deleted
Total expenses: 23 baht
Total expenses for month June: 23 baht
```

[Previous Workshop](../workshop_002/readme.md) | [Next Workshop](../workshop_004/readme.md)
