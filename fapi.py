from fastapi import FastAPI, Path
import json
import pandas as pd


app = FastAPI()


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    },
    2: {
        "name": "Eggs",
        "price": 2.99,
        "brand": "Regular"
    }
}

@app.get("/")
def home():
    return {"Data": "Testing"}


@app.get("/about")
def about():
    return {"Data": "About"}



@app.get("/help")
def help():
    return {"Data": "This is help !"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None,description="This is Item ID")):
    return inventory[item_id]


@app.get("/labels")
def label():
    df = pd.read_csv("df_error.csv")
    jsonString = json.dumps(list(df))
    return jsonString