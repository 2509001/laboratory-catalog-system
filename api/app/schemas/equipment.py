from pydantic import BaseModel


class EquipmentResponse(BaseModel):
    equipment_id: str
    name: str
    brand: str | None = None
    model: str | None = None
    operational_status: str

    class Config:
        from_attributes = True