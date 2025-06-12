# Python Workshop: Let's Talk Type Hints 🐍✨

Hey there! Welcome to our Python workshop. Today, we’re diving into something simple but super helpful: **type hints**. These little additions to your code can make your life way easier — especially when your project grows or you're working in a team.

---

## Step 1: Starting Without Type Hints

Let’s kick things off with a basic function. Nothing fancy, just putting together a full name.

```python
def get_full_name(first_name, last_name):
    full_name = first_name.title() + "" + last_name.title()
    return full_name

print(get_full_name("john", "doe"))
```

### 🤔 What’s the deal?

This works, sure. But there’s a catch:
- We have no idea what type of data `first_name` and `last_name` are supposed to be.
- If someone passes a number instead of a string? Boom 💥 — unexpected bugs.
- Your editor or linter can’t help much because there’s no hint about what’s expected.

---

## Step 2: Now With Type Hints (So Much Better!)

Let’s toss the old version and write it again, but this time we’ll tell Python what types we expect.

```python
def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + "" + last_name.title()
    return full_name

print(get_full_name("john", "doe"))
```

### 💡 Why this is awesome:

- **Catches bugs early**: If you pass the wrong type, tools can warn you before you even run the code.
- **Smarter editor help**: Autocomplete, suggestions, and error checking just got way better.
- **Clearer for everyone**: Anyone reading your code knows exactly what to expect.

---

## Quick Recap

Type hints in Python:
- Help prevent silly mistakes ✅
- Make your code easier to read and maintain 🧼
- Play nicely with your editor and tools 🤝

Give them a try in your next project — your future self will thank you!

Happy coding! 🐍💻
