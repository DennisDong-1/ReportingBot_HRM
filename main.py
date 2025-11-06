from fastapi import FastAPI

var = FastAPI()

@var.get("/")
def root():
    return {"question": "Show me who is on leave today."}

# @var.get("/test")
# def root():
#     return {"Hello": "World"}

# @var.post("/items")
# def create_item(item: str):
#     items.append(item)
#     return items

# @var.get("/items/{item_id}")
# def get_item(item_id: int) -> str:
#     item = items[item_id]
#     return item
