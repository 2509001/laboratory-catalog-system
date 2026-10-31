from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Equipment(Base):
    __tablename__ = "equipment"

    equipment_id = Column(UUID(as_uuid=True), primary_key=True)

    official_inventory_number = Column(String(50))

    internal_lab_number = Column(String(50))

    name = Column(String(255))

    brand = Column(String(100))

    model = Column(String(100))

    serial_number = Column(String(100))

    location = Column(String(100))

    operational_status = Column(String(50))