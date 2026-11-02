from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import engine
from app.schemas.equipment import EquipmentCreate

router = APIRouter()


@router.get("/equipment")
def get_equipment():

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    equipment_id,
                    official_inventory_number,
                    internal_lab_number,
                    name,
                    brand,
                    model,
                    location,
                    operational_status
                FROM equipment
            """)
        )

        rows = result.mappings().all()

        return rows


@router.get("/equipment/{equipment_id}")
def get_equipment_by_id(equipment_id: str):

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    equipment_id,
                    name,
                    brand,
                    model,
                    operational_status
                FROM equipment
                WHERE equipment_id = :equipment_id
            """),
            {
                "equipment_id": equipment_id
            }
        )

        row = result.mappings().first()

        if row is None:
            return {
                "error": "Equipment not found"
            }

        return row


@router.post("/equipment")
def create_equipment(equipment: EquipmentCreate):

    return {
        "message": "Equipment received successfully",
        "equipment": equipment.model_dump()
    }