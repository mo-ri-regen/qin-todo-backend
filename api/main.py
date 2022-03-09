from fastapi import FastAPI
from api.router import task
app = FastAPI()

app.include_router(task.router)

@app.get("/hello")
async def hello():
    return {"message": "hello world!"}