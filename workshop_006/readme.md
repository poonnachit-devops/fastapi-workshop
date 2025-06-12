# 🐍 FastAPI Local CRUD Tutorial

Welcome to this mini-project where you'll learn how to build a simple local CRUD (Create, Read, Update, Delete) API using **FastAPI** and **Pydantic**.

## Pre-requisites
this workshop assumes you have completed [workshop_005](../workshop_005/readme.md) and have running fastapi server, if you haven't done so, please complete the previous workshop first.

## 🛠️ Project Structure

All code is written in `main.py`. Here's what it does:

### ✅ Root Route

```python
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Returns a welcome message. Great for testing the server is running.

---

## 🧱 The Models

```python
class Item(BaseModel):
    item_id: int
    name: str
    description: str | None = None
    price: float
```

This is the full item data including `item_id`.

```python
class ItemDto(BaseModel):
    name: str
    description: str | None = None
    price: float
```

This is the input data for creating/updating an item (no ID yet).

---

## 📦 In-Memory Storage

```python
items: dict[int, Item] = {}
id = 0
```

We store items in a Python dictionary. Each item has a unique integer ID.

---

## 🔄 CRUD Endpoints

### 📥 Create an Item

```python
@app.post("/items/", response_model=Item)
def create_item(item: ItemDto):
```

- Adds a new item.
- Auto-increments the `item_id`.
- Example input:
  ```json
  {
    "name": "Notebook",
    "description": "A spiral notebook",
    "price": 3.99
  }
  ```

### 📤 Read All Items

```python
@app.get("/items/", response_model=list[Item])
def read_items():
```

- Returns a list of all items.

### 🔍 Read One Item

```python
@app.get("/items/{item_id}", response_model=Item | dict)
def read_item(item_id: int):
```

- Returns the item by ID, or an error message if not found.

### 📝 Update an Item

```python
@app.put("/items/{item_id}", response_model=Item | dict)
def update_item(item_id: int, item: ItemDto):
```

- Replaces an item with new data.
- If the item ID doesn't exist, returns an error.

### ❌ Delete an Item

```python
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
```

- Deletes an item by ID.
- Returns a success message or an error if not found.

---

## 📘 Example Usage

You can test all endpoints using the Swagger UI at:

👉 [http://localhost:8000/docs](http://localhost:8000/docs)

Or use a tool like `curl`, `Postman`, or any HTTP client.

---

## 🧠 What's Next?

- Add validation (e.g., price must be > 0)
- Save data to a file or database
- Use UUIDs instead of integers for IDs
- Create users and authentication

---

Happy coding! 🚀  