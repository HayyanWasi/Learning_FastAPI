from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}


# @app.get("/items/{item_id}")
# async def read_item(item_id:int):
#     return {"item_id": item_id}


# @app.get("/items{item_id}")
# async def read_item(item_id: int, q: str | None = None):
#     result = {"item_id": item_id}
#     if q:
#         result["q"] = q
#     return result

from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None=None
    price: float
    tax: float | None = None
    create_item: str


@app.post("/items/{item_id}")
async def create_item(item: Item, item_id: int, q:str | None=None):
    item_dict = item.dict()
    if item.tax is not None:
        item_dict["price_with_tax"] = item.price + item.tax
    return item_dict





@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()  
    if item.tax is not None:
        item_dict["price_with_tax"] = item.price + item.tax
    return item_dict




# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str | None = None):
#     """
#     GET /items/{item_id}
#       - item_id: required path parameter, must be int
#       - q: optional query parameter, string or None
#     """
#     result = {"item_id": item_id}
#     if q:
#         result["q"] = q  # include query text if provided
#     return result



@app.put("/items/{item_id}")
async def update_item( item_id: int,item: Item, q: str | None = None):
    result =  {"item_id": item_id, **item.dict()}
    if q:
        result = result["q"] = q
    return q



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)