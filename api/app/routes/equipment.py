from uuid import uuid4

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
                    official_inventory_number,
                    internal_lab_number,
                    name,
                    brand,
                    model,
                    location,
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

    equipment_id = str(uuid4())

    with engine.connect() as connection:

        connection.execute(
            text("""
                INSERT INTO equipment (
                    equipment_id,
                    official_inventory_number,
                    internal_lab_number,
                    name,
                    brand,
                    model,
                    location,
                    operational_status,
                    category_id
                )
                VALUES (
                    :equipment_id,
                    :official_inventory_number,
                    :internal_lab_number,
                    :name,
                    :brand,
                    :model,
                    :location,
                    :operational_status,
                    :category_id
                )
            """),
            {
                "equipment_id": equipment_id,
                "official_inventory_number": equipment.official_inventory_number,
                "internal_lab_number": equipment.internal_lab_number,
                "name": equipment.name,
                "brand": equipment.brand,
                "model": equipment.model,
                "location": equipment.location,
                "operational_status": equipment.operational_status,
                "category_id": equipment.category_id
            }
        )

        connection.commit()

    return {
        "message": "Equipment created successfully",
        "equipment_id": equipment_id
    }


@router.patch("/equipment/{equipment_id}/status")
def update_equipment_status(
    equipment_id: str,
    status_update: EquipmentStatusUpdate
):

    with engine.connect() as connection:

        connection.execute(
            text("""
                UPDATE equipment
                SET operational_status = :status
                WHERE equipment_id = :equipment_id
            """),
            {
                "status": status_update.operational_status,
                "equipment_id": equipment_id
            }
        )

        connection.commit()

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

    maintenance_id = str(uuid4())

    with engine.connect() as connection:

        connection.execute(
            text("""
                INSERT INTO maintenance_records (
                    maintenance_id,
                    equipment_id,
                    maintenance_date,
                    maintenance_type,
                    description
                )
                VALUES (
                    :maintenance_id,
                    :equipment_id,
                    :maintenance_date,
                    :maintenance_type,
                    :description
                )
            """),
            {
                "maintenance_id": maintenance_id,
                "equipment_id": equipment_id,
                "maintenance_date": maintenance.maintenance_date,
                "maintenance_type": maintenance.maintenance_type,
                "description": maintenance.description
            }
        )

        connection.commit()

    return {
        "message": "Maintenance record created",
        "maintenance_id": maintenance_id,
        "equipment_id": equipment_id
    }