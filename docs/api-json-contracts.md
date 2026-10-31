# API JSON Contracts

## Equipment

### GET /equipment/{id}

Response

```json
{
  "equipmentId": "uuid",
  "officialInventoryNumber": "UPY-001",
  "internalLabNumber": "LAB-001",
  "name": "Oscilloscope ATTEN ADS1022CL",
  "brand": "ATTEN",
  "model": "ADS1022CL",
  "serialNumber": "SN123456",
  "location": "Electronics Laboratory",
  "operationalStatus": "Operational",
  "category": {
    "categoryId": "uuid",
    "name": "Measurement Equipment"
  }
}
```

---

### POST /equipment

Request

```json
{
  "officialInventoryNumber": "UPY-001",
  "internalLabNumber": "LAB-001",
  "name": "Oscilloscope ATTEN ADS1022CL",
  "brand": "ATTEN",
  "model": "ADS1022CL",
  "serialNumber": "SN123456",
  "location": "Electronics Laboratory",
  "operationalStatus": "Operational",
  "categoryId": "uuid"
}
```

Response

```json
{
  "message": "Equipment created successfully",
  "equipmentId": "uuid"
}
```

---

## Category

### GET /categories

Response

```json
[
  {
    "categoryId": "uuid",
    "name": "Measurement Equipment"
  }
]
```

---

## Maintenance Record

### POST /equipment/{id}/maintenance

Request

```json
{
  "maintenanceDate": "2026-10-30",
  "maintenanceType": "Preventive",
  "description": "Routine inspection and cleaning"
}
```

Response

```json
{
  "message": "Maintenance record created successfully"
}
```

---

## Datasheet

### POST /equipment/{id}/datasheets

Request

```json
{
  "documentName": "ATTEN ADS1022CL Datasheet",
  "filePath": "/docs/datasheets/atten_ads1022cl.pdf"
}
```

Response

```json
{
  "message": "Datasheet uploaded successfully"
}
```

---

## Error Response

```json
{
  "error": "Resource not found",
  "status": 404
}
```