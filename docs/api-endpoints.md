# API Endpoint Mapping

## Purpose

This document maps functional requirements to REST API endpoints for the Laboratory Catalog System.

---

# Equipment

## Get all equipment

GET /equipment

Description:
Returns all equipment registered in the catalog.

Related Requirements:
- FR-01 Search Equipment

---

## Get equipment by ID

GET /equipment/{id}

Description:
Returns detailed information about a specific equipment item.

Related Requirements:
- FR-02 View Equipment Details

---

## Create equipment

POST /equipment

Description:
Creates a new equipment record.

Related Requirements:
- FR-07 Register Equipment

---

## Update equipment

PUT /equipment/{id}

Description:
Updates an existing equipment record.

Related Requirements:
- FR-04 Update Equipment Information

---

## Delete equipment

DELETE /equipment/{id}

Description:
Removes an equipment record.

---

# Categories

## Get all categories

GET /categories

Description:
Returns all equipment categories.

---

## Get category by ID

GET /categories/{id}

Description:
Returns category details.

---

# Maintenance Records

## Get equipment maintenance history

GET /equipment/{id}/maintenance

Description:
Returns maintenance records for a piece of equipment.

Related Requirements:
- FR-08 Maintenance Tracking

---

## Create maintenance record

POST /equipment/{id}/maintenance

Description:
Creates a maintenance record associated with equipment.

Related Requirements:
- FR-08 Maintenance Tracking

---

# Datasheets

## Get equipment datasheets

GET /equipment/{id}/datasheets

Description:
Returns technical documents associated with equipment.

Related Requirements:
- FR-03 Technical Documentation

---

## Upload datasheet

POST /equipment/{id}/datasheets

Description:
Associates technical documentation with equipment.

Related Requirements:
- FR-03 Technical Documentation