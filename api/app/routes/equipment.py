from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import engine
from app.schemas.equipment import (
    EquipmentCreate,
    EquipmentStatusUpdate,
    MaintenanceCreate
)

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


@router.patch("/equipment/{equipment_id}/status")
def update_equipment_status(
    equipment_id: str,
    status_update: EquipmentStatusUpdate
):

    return {
        "message": "Equipment status updated",
        "equipment_id": equipment_id,
        "new_status": status_update.operational_status
    }

@router.post("/equipment/{equipment_id}/maintenance")
def create_maintenance(
    equipment_id: str,
    maintenance: MaintenanceCreate
):

    return {
        "message": "Maintenance record created",
        "equipment_id": equipment_id,
        "maintenance": maintenance.model_dump()
    }