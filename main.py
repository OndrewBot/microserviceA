from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/convert")
def read_item(units: str, amount: float, target: str):
    known_units = {"cups", "tbs", "tsp"}
    if (units not in known_units)or (target not in known_units) :
        return {"invalid units - must be 'cups', 'tbs', 'tsp'"}
    if units == target:
        return {"units": units, "amount": amount}
    if units == "cups":
        if target == "tbs":
            amount = amount * 16
        elif target == "tsp":
            amount = amount * 48
    elif units == "tbs":
        if target == "cups":
            amount = round(amount / 16, 2)
        elif target == "tsp":
            amount = amount * 3
    elif units == "tsp":
        if target == "tbs":
            amount = round(amount / 3, 2)
        elif target == "cups":
            amount = round(amount / 48, 2)
    
    return {"units": target, "amount": amount}