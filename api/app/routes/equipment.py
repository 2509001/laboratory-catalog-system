from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import engine

router = APIRouter()


@router.get("/equipment")
def get_equipment():

    with engine.connect() as connection:

        result = connection.execute(
            text(
                """
                SELECT
                    equipment_id,
                    name,
                    brand,
                    model,
                    operational_status
                FROM equipment
                """
            )
        )

        rows = result.mappings().all()

        return rows