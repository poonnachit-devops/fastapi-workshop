# FastAPI Error Handling

Welcome to the FastAPI Error Handling workshop! In this mini-project, you'll learn how to handle errors gracefully in your FastAPI application.

## Prre-requisites
This workshop assumes you have completed [workshop_006](../workshop_006/readme.md) and have a running FastAPI server. If you haven't done so, please complete the previous workshop first.

## 🛠️ Project Structure
All code is written in `main.py`. Here's what it does:

## Import Http Exception
```python
from fastapi import FastAPI, HTTPException
```

## Fix path read one item to handle errors correctly
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
```
if the item ID does not exist, it raises a `404 Not Found` error with a custom message.

## Update an Item
```python
@app.put("/items/{item_id}")
async def update_item(item_id: int, item_dto: ItemDto):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = Item(item_id=item_id, **item_dto.dict())
    return items[item_id]
```

This endpoint updates an existing item. If the item ID does not exist, it raises a `404 Not Found` error.

## Delete an Item
```python
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted successfully"}
```
This endpoint deletes an item by its ID. If the item ID does not exist, it raises a `404 Not Found` error.


