from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from calculator import calculate as calc_fn

app = FastAPI()

# Serve static folder (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/calculate")
def calculate(a: float, b: float, op: str):
    try:
        result = calc_fn(a, b, op)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
