# Catalog List and Equipment Profile Design

## Equipment Catalog Screen

Purpose:
Allow users to browse and locate laboratory equipment.

---

## Layout

+--------------------------------------------------+
| Search Bar                                       |
+--------------------------------------------------+

+--------------------------------------------------+
| Filters                                          |
| - Category                                       |
| - Operational Status                             |
+--------------------------------------------------+

+--------------------------------------------------+
| Equipment Table                                  |
+--------------------------------------------------+

| Inventory | Name | Brand | Status | Details |
|------------|------|--------|---------|---------|
| UPY-001 | Oscilloscope | ATTEN | Operational | View |

---

## User Actions

- View equipment details
- Search equipment
- Filter by category
- Filter by status

---

## Equipment Summary Information

Displayed Fields:

- Official Inventory Number
- Internal Lab Number
- Name
- Brand
- Model
- Operational Status

---

# Equipment Profile Screen

Purpose:
Display complete information for a selected equipment item.

---

## General Information Section

Fields:

- Official Inventory Number
- Internal Lab Number
- Name
- Brand
- Model
- Serial Number
- Location
- Operational Status

---

## Maintenance Section

Displays:

- Maintenance Date
- Maintenance Type
- Description

Actions:

- Add Maintenance Record

---

## Datasheets Section

Displays:

- Document Name
- File Path

Actions:

- View Datasheet
- Upload Datasheet

---

## Navigation Flow

Catalog List
    |
    +---- Equipment Profile
              |
              +---- Maintenance History
              |
              +---- Datasheets

---

## Responsive Design

Desktop:
- Table-based catalog
- Side-by-side profile sections

Tablet:
- Responsive cards

Mobile:
- Vertical stacked layout
- Expandable sections