# from fastapi import APIRouter
from app.routers import items
from fastapi import FastAPI
import uvicorn
import numpy as np


app = FastAPI()


@app.get("/")
def root():
    ret = np.random.choice(items.easy)
    return {'result': ret}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8051)
