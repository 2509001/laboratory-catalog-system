from fastapi import APIRouter

from app.schemas.role import RoleCreate

router = APIRouter()


@router.get("/roles")
def get_roles():

    return [
        {
            "name": "Administrator"
        },
        {
            "name": "Laboratory Staff"
        },
        {
            "name": "Coordinator"
        },
        {
            "name": "Student"
        }
    ]


@router.post("/roles")
def create_role(
    role: RoleCreate
):

    return {
        "message": "Role created successfully",
        "role": role.model_dump()
    }