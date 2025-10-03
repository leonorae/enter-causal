from typing import Union
from fastapi import FastAPI
import hello_dowhy

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/model/identified_estimand")
def identified_estimand():
    return {"identified_estimand": str(hello_dowhy.identified_estimand)}

@app.get("/model/estimate")
def estimate():
    return {"estimate": str(hello_dowhy.estimate)}

@app.get("/model/refute")
def refute():
    return {"refute": str(hello_dowhy.refute_results)}
