# Laboratory Catalog System API Specification

Version: 1.0

## Base URL

/api/v1

---

# Equipment

## GET /equipment

Description:
Returns all equipment records.

Response:
200 OK

---

## GET /equipment/{id}

Description:
Returns a specific equipment item.

Response:
200 OK

404 Not Found

---

## POST /equipment

Description:
Creates a new equipment record.

Response:
201 Created

400 Bad Request

409 Conflict

---

## PUT /equipment/{id}

Description:
Updates equipment information.

Response:
200 OK

404 Not Found

---

## DELETE /equipment/{id}

Description:
Deletes an equipment record.

Response:
204 No Content

404 Not Found

---

# Categories

## GET /categories

Description:
Returns all categories.

Response:
200 OK

---

## GET /categories/{id}

Description:
Returns category details.

Response:
200 OK

404 Not Found

---

# Maintenance Records

## GET /equipment/{id}/maintenance

Description:
Returns maintenance history.

Response:
200 OK

404 Not Found

---

## POST /equipment/{id}/maintenance

Description:
Creates a maintenance record.

Response:
201 Created

400 Bad Request

404 Not Found

---

# Datasheets

## GET /equipment/{id}/datasheets

Description:
Returns equipment documents.

Response:
200 OK

404 Not Found

---

## POST /equipment/{id}/datasheets

Description:
Uploads a datasheet.

Response:
201 Created

400 Bad Request

404 Not Found

---

# Standard Responses

200 OK

201 Created

204 No Content

400 Bad Request

404 Not Found

409 Conflict

500 Internal Server Error