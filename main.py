from asyncio import run
import uvicorn
from fastapi import FastAPI, APIRouter

from database.init_db import create_database
from views import assets_router, measurementservice_router

app = FastAPI()
router = APIRouter()

@app.router.get('/')
def first():
    return "Hello World"

app.include_router(prefix='/first', router=router)
app.include_router(assets_router)
app.include_router(measurementservice_router)

if __name__=='__main__':
    run(create_database())
    uvicorn.run(app)