# Python Workshop: Let’s Talk Type Hints 🐍✨

Hey there! Welcome to our Python workshop. Today, we’re going to explore some common Python **type hints** for everyday data types. Adding type hints to your functions makes your code clearer, easier to maintain, and helps catch bugs early. Ready? Let’s go!

---

## Step 1: String (`str`)

Let’s start with the basics: a function that greets someone by name.

```python
def greeting(name: str) -> str:
    return f"Hello, {name}!"

print(greeting("World"))
```
### 🤔 What’s happening here?
- `name: str` means the function expects name to be a string.

- `-> str` means the function returns a string.

- If you accidentally pass a number instead of a string, your tools will let you know!
---

## Step 2: Integer (int)
Next up, we’ll repeat a string a certain number of times.
```python
def repeat_string(s: str, times: int) -> str:
    """Repeat a string multiple times."""
    return s * times

print(repeat_string("Hi ", 3))  # Output: Hi Hi Hi 
```

### 💡 Why it helps
- `times: int` means you must give an integer number for how many times to repeat.

- Type hints keep things clear and avoid weird bugs like passing a float or string here by mistake.

---

## Step 3: List (List[int])
What if you want to grab the first item from a list of numbers?

```python
def get_first_item(items: List[int]) -> int:
    return items[0]

print(get_first_item([10, 20, 30]))  # Output: 10
```
### 🤓 Notes:
- `List[int]` means a list where all items are integers.

- This helps readers and tools know what kind of list you expect.

---

## Step 4: Dictionary (Dict[str, str])
How about getting a capital city from a dictionary?

```python
def get_capital(countries: Dict[str, str], country: str) -> str:
    return countries[country]

capitals = {"France": "Paris", "Japan": "Tokyo"}
print(get_capital(capitals, "France"))  # Output: Paris
```

### 🤓 Notes:
- `Dict[str, str]` means keys are strings (country names), values are strings (capitals).

---

## Step 5: Set (Set[int])
Sets hold unique items. Let’s check for duplicates by comparing a list to its set.

```python
def has_duplicates(items: Set[int]) -> bool:
    return len(items) != len(set(items))

print(has_duplicates([1, 2, 2, 3]))  # Output: True
```
While here we didn’t type hint the set explicitly, you can use `Set[int]` to represent sets of integers.

---

## Step 6: Tuple (Tuple[str, int])
Tuples are fixed-length collections. For example, user info might be a name and age:

```python
from typing import Tuple

def get_user_info() -> Tuple[str, int]:
    return ("Alice", 30)

name, age = get_user_info()
print(name)  # Alice
print(age)   # 30
```
`Tuple[str, int]` means a two-item tuple with a string first and an integer second.

---

# Quick Recap
| Type  | Example Hint     | What it Means                      |
|-------|------------------|----------------------------------|
| str   | `name: str`      | A text string                    |
| int   | `times: int`     | An integer number                |
| List  | `List[int]`      | A list of integers              |
| Dict  | `Dict[str, str]` | A dictionary with string keys/values |
| Set   | `Set[int]`       | A set of unique integers        |
| Tuple | `Tuple[str, int]`| A fixed-length pair (string, int) |


## Why Use Type Hints?
- 🚫 Catch mistakes before running your code
- 🔍 Make your code easier to read and understand
- 🤖 Boost your editor’s autocomplete and error checking

Give it a shot on your next Python project — your future self will thank you!

Happy coding! 🐍💻

[Previous Workshop](../workshop_001/readme.md) | [Next Workshop](../workshop_003/readme.md)
```