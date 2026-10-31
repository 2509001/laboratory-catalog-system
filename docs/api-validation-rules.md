# API Validation Rules and Error Handling

## Purpose

This document defines validation rules and standard error responses for the Laboratory Catalog System API.

---

# Equipment Validation Rules

## Equipment Name

Rule:
Equipment name is required.

Response:

```json
{
  "error": "Equipment name is required",
  "status": 400
}
```

---

## Category

Rule:
The category must exist before equipment can be created.

Response:

```json
{
  "error": "Category not found",
  "status": 404
}
```

---

## Official Inventory Number

Rule:
Official inventory number must be unique.

Response:

```json
{
  "error": "Official inventory number already exists",
  "status": 409
}
```

---

## Internal Lab Number

Rule:
Internal lab number must be unique.

Response:

```json
{
  "error": "Internal lab number already exists",
  "status": 409
}
```

---

## Equipment Identifier

Rule:
At least one identifier must be provided.

Required:

- officialInventoryNumber
OR
- internalLabNumber

Response:

```json
{
  "error": "At least one equipment identifier is required",
  "status": 400
}
```

---

# Maintenance Validation Rules

## Equipment Exists

Rule:
Maintenance records can only be created for existing equipment.

Response:

```json
{
  "error": "Equipment not found",
  "status": 404
}
```

---

## Maintenance Type

Allowed Values:

- Preventive
- Corrective
- Calibration
- Inspection

Response:

```json
{
  "error": "Invalid maintenance type",
  "status": 400
}
```

---

# Datasheet Validation Rules

## Document Name

Rule:
Document name is required.

Response:

```json
{
  "error": "Document name is required",
  "status": 400
}
```

---

# Standard HTTP Responses

## Success

200 OK

```json
{
  "message": "Request completed successfully"
}
```

---

## Created

201 Created

```json
{
  "message": "Resource created successfully"
}
```

---

## Bad Request

400 Bad Request

```json
{
  "error": "Invalid request"
}
```

---

## Not Found

404 Not Found

```json
{
  "error": "Resource not found"
}
```

---

## Conflict

409 Conflict

```json
{
  "error": "Duplicate resource"
}
```

---

## Internal Server Error

500 Internal Server Error

```json
{
  "error": "Unexpected server error"
}
```