from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

class Item(BaseModel):
    item_id: int
    name: str
    description: str | None = None
    price: float

class ItemDto(BaseModel):
    name: str
    description: str | None = None
    price: float


items: dict[int, Item] = {}
id = 0

@app.post("/items/", response_model=Item)
def create_item(item: ItemDto):
    global id
    id += 1

    items[id] = Item(item_id=id, **item.model_dump())
    return items[id]


@app.get("/items/", response_model=list[Item])
def read_items():
    return list(items.values())

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemDto):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = Item(item_id=item_id, **item.model_dump())
    return items[item_id]

@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted successfully"}