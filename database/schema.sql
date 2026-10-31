-- =====================================================
-- Laboratory Catalog System (LCS)
-- Database Schema
-- PostgreSQL
-- =====================================================

-- ==========================================
-- TABLE: roles
-- ==========================================

CREATE TABLE roles (
    role_id UUID PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255)
);

-- ==========================================
-- TABLE: users
-- ==========================================

CREATE TABLE users (
    user_id UUID PRIMARY KEY,

    first_name VARCHAR(100) NOT NULL,

    last_name VARCHAR(100) NOT NULL,

    email VARCHAR(255) NOT NULL UNIQUE,

    role_id UUID NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_users_roles
    FOREIGN KEY (role_id)
    REFERENCES roles(role_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- ==========================================
-- TABLE: categories
-- ==========================================

CREATE TABLE categories (
    category_id UUID PRIMARY KEY,

    name VARCHAR(100) NOT NULL UNIQUE,

    description TEXT
);

-- ==========================================
-- TABLE: equipment
-- ==========================================

CREATE TABLE equipment (

    equipment_id UUID PRIMARY KEY,

    official_inventory_number VARCHAR(50) UNIQUE,

    internal_lab_number VARCHAR(50) UNIQUE,

    name VARCHAR(255) NOT NULL,

    brand VARCHAR(100),

    model VARCHAR(100),

    serial_number VARCHAR(100),

    description TEXT,

    location VARCHAR(100) NOT NULL,

    operational_status VARCHAR(50) NOT NULL,

    acquisition_date DATE,

    qr_code_url TEXT,

    category_id UUID NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_equipment_category
    FOREIGN KEY (category_id)
    REFERENCES categories(category_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT

    CONSTRAINT chk_equipment_status
        CHECK (
            operational_status IN (
                'Operational',
                'Under Maintenance',
                'Out of Service',
                'Reserved',
                'Pending Inspection',
                'Retired'
            )
        ),

    CONSTRAINT chk_equipment_identifier
        CHECK (
            official_inventory_number IS NOT NULL
            OR internal_lab_number IS NOT NULL
)
);

-- ==========================================
-- TABLE: maintenance_records
-- ==========================================

CREATE TABLE maintenance_records (

    maintenance_id UUID PRIMARY KEY,

    equipment_id UUID NOT NULL,

    maintenance_date DATE NOT NULL,

    maintenance_type VARCHAR(50) NOT NULL,

    status_before VARCHAR(50),

    status_after VARCHAR(50),

    description TEXT NOT NULL,

    technician VARCHAR(255),

    observations TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_maintenance_equipment
    FOREIGN KEY (equipment_id)
    REFERENCES equipment(equipment_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE

    CONSTRAINT chk_maintenance_type
        CHECK (
            maintenance_type IN (
                'Preventive',
                'Corrective',
                'Calibration',
                'Inspection'
            )
        )
);

-- ==========================================
-- TABLE: datasheets
-- ==========================================

CREATE TABLE datasheets (

    datasheet_id UUID PRIMARY KEY,

    equipment_id UUID NOT NULL,

    document_name VARCHAR(255) NOT NULL,

    file_path TEXT NOT NULL,

    document_type VARCHAR(50),

    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_datasheet_equipment
    FOREIGN KEY (equipment_id)
    REFERENCES equipment(equipment_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

-- ==========================================
-- INDEXES
-- ==========================================

CREATE INDEX idx_users_email
ON users(email);

CREATE INDEX idx_equipment_name
ON equipment(name);

CREATE INDEX idx_equipment_brand
ON equipment(brand);

CREATE INDEX idx_equipment_model
ON equipment(model);

CREATE INDEX idx_equipment_status
ON equipment(operational_status);

CREATE INDEX idx_equipment_category
ON equipment(category_id);

CREATE INDEX idx_maintenance_date
ON maintenance_records(maintenance_date);

CREATE INDEX idx_maintenance_equipment
ON maintenance_records(equipment_id);

CREATE INDEX idx_datasheet_equipment
ON datasheets(equipment_id);