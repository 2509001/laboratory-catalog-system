from uuid import uuid4

from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import engine
from app.schemas.role import RoleCreate

router = APIRouter()


@router.get("/roles")
def get_roles():

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    role_id,
                    name,
                    description
                FROM roles
            """)
        )

        roles = result.mappings().all()

        return roles


@router.post("/roles")
def create_role(role: RoleCreate):

    role_id = str(uuid4())

    with engine.connect() as connection:

        connection.execute(
            text("""
                INSERT INTO roles (
                    role_id,
                    name,
                    description
                )
                VALUES (
                    :role_id,
                    :name,
                    :description
                )
            """),
            {
                "role_id": role_id,
                "name": role.name,
                "description": role.description
            }
        )

        connection.commit()

    return {
        "message": "Role created successfully",
        "role_id": role_id
    }