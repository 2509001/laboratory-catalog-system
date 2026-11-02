from pydantic import BaseModel


class DatasheetCreate(BaseModel):
    document_name: str
    file_path: str