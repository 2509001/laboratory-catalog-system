from fastapi import APIRouter

from app.schemas.datasheet import DatasheetCreate

router = APIRouter()


@router.get("/equipment/{equipment_id}/datasheets")
def get_datasheets(equipment_id: str):

    return {
        "equipment_id": equipment_id,
        "datasheets": [
            {
                "document_name": "Oscilloscope Datasheet",
                "file_path": "/docs/oscilloscope.pdf"
            }
        ]
    }


@router.post("/equipment/{equipment_id}/datasheets")
def create_datasheet(
    equipment_id: str,
    datasheet: DatasheetCreate
):

    return {
        "message": "Datasheet uploaded successfully",
        "equipment_id": equipment_id,
        "datasheet": datasheet.model_dump()
    }