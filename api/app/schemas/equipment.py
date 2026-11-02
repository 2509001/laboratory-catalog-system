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


class EquipmentStatusUpdate(BaseModel):
    operational_status: str

class MaintenanceCreate(BaseModel):
    maintenance_date: str
    maintenance_type: str
    description: str