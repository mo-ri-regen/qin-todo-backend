from fastapi import APIRouter


router = APIRouter()

@router.get("/todo/{id}")
async def get_task():
    pass

@router.post("/todo")
async def add_task():
    pass

@router.put("/todo/{id}")
async def edit_task():
    pass

@router.delete("/todo/{id}")
async def delete_task():
    pass
