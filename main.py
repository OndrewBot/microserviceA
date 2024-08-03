from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

known_units = set("cups", "tbs", "tsp")

@app.get("/convert/units:{units}+amount:{amount}+target-units:{target}")
def read_item(units: str, amount: int, target: str):
    if (units not in known_units)or (target not in known_units) :
        return {"invalid units - must be 'cups', 'tbs', 'tsp'"}
    if units == target:
        return {"units": units, "amount": amount}
    if units == "cups":
        if target == "tbs":
            amount = amount * 16
        elif target == "tsp":
            pass
    elif units == "tbs":
        pass
    elif units == "tsp":
        pass
    
    return {"units": units, "amount": amount}