from fastapi import FastAPI

from app.routes.equipment import router as equipment_router
from app.routes.roles import router as roles_router

app = FastAPI(
    title="Laboratory Catalog System API",
    version="1.0"
)

app.include_router(equipment_router)
app.include_router(roles_router)


@app.get("/")
def root():
    return {
        "message": "Laboratory Catalog System API"
    }