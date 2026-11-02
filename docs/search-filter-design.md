# Search, Dual Filtering and Status Design

## Purpose

Provide users with efficient mechanisms to locate laboratory equipment using multiple search and filtering criteria.

---

# Search Functionality

## Search Bar

Users can search equipment using:

- Official Inventory Number
- Internal Lab Number
- Equipment Name
- Brand
- Model

Example Searches:

- UPY-001
- LAB-001
- Oscilloscope
- ATTEN
- CD772

---

# Dual Identification Filtering

The system supports dual classification identifiers.

## Official Inventory Number

Purpose:
Institutional inventory tracking.

Examples:

- UPY-001
- UPY-002

---

## Internal Laboratory Number

Purpose:
Local laboratory management.

Examples:

- LAB-001
- LAB-002

---

# Category Filter

Users can filter equipment by category.

Categories:

- Measurement Equipment
- Development Boards
- Computers
- Specialized Machinery
- Tools
- Cables
- Soldering Equipment

---

# Operational Status Filter

Users can filter equipment by status.

Available Statuses:

- Operational
- Under Maintenance
- Out of Service
- Reserved
- Pending Inspection
- Retired

---

# Combined Filtering

Users may combine filters.

Examples:

Category:
Measurement Equipment

Status:
Operational

Result:
Only operational measurement equipment is displayed.

---

# User Interface Components

## Search Bar

Position:
Top of catalog screen.

Behavior:
Real-time filtering or search button action.

---

## Filter Panel

Components:

- Category Dropdown
- Status Dropdown
- Reset Filters Button

---

## Results Area

Displays:

- Equipment Name
- Inventory Numbers
- Status
- Category
- Details Button

---

# Responsive Design

Desktop:
- Search + Filters displayed horizontally.

Tablet:
- Filters displayed as collapsible panel.

Mobile:
- Search input on top.
- Filters hidden inside expandable menu.