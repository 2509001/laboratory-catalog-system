from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.equipment import router as equipment_router
from app.routes.roles import router as roles_router
from app.routes.datasheets import router as datasheets_router

app = FastAPI(
    title="Laboratory Catalog System API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(equipment_router)
app.include_router(roles_router)
app.include_router(datasheets_router)


@app.get("/")
def root():
    return {
        "message": "Laboratory Catalog System API"
    }