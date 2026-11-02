from pydantic import BaseModel


class EquipmentCreate(BaseModel):
    official_inventory_number: str | None = None
    internal_lab_number: str | None = None

    name: str
    brand: str | None = None
    model: str | None = None

    location: str
    operational_status: str

    category_id: str