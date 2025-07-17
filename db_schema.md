# Vehicle Parking App – Database Structure & Dashboard Planning

## 📊 Overview
This document outlines the database schema and how it supports key dashboard features for users and admins in a vehicle parking system.

---

## 🗂️ Table Structures

### 1. Users
| Column Name  | Data Type | Constraints         |
|--------------|------------|---------------------|
| id           | INTEGER    | PRIMARY KEY         |
| username     | TEXT       | UNIQUE, NOT NULL    |
| email        | TEXT       | UNIQUE, NOT NULL    |
| password     | TEXT       | NOT NULL            |
| is_admin     | BOOLEAN    | DEFAULT FALSE       |

---

### 2. ParkingLots
| Column Name              | Data Type | Constraints         |
|--------------------------|------------|---------------------|
| id                       | INTEGER    | PRIMARY KEY         |
| prime_location_name      | TEXT       | NOT NULL            |
| address                  | TEXT       | NOT NULL            |
| pin_code                 | TEXT       | NOT NULL            |
| price_per_unit_time      | FLOAT      | NOT NULL            |
| maximum_number_of_spots  | INTEGER    | NOT NULL            |

---

### 3. ParkingSpots
| Column Name | Data Type | Constraints                                          |
|-------------|------------|------------------------------------------------------|
| id          | INTEGER    | PRIMARY KEY                                          |
| lot_id      | INTEGER    | FOREIGN KEY → ParkingLots(id), NOT NULL             |
| status      | TEXT       | CHECK (status IN ('A', 'O')), DEFAULT 'A'           |

---

### 4. Reservations
| Column Name        | Data Type | Constraints                                      |
|--------------------|-----------|--------------------------------------------------|
| id                 | INTEGER   | PRIMARY KEY                                     |
| spot_id            | INTEGER   | FOREIGN KEY → ParkingSpots(id), NOT NULL       |
| user_id            | INTEGER   | FOREIGN KEY → Users(id), NOT NULL              |
| parking_timestamp  | DATETIME  | DEFAULT CURRENT_TIMESTAMP                      |
| leaving_timestamp  | DATETIME  | NULLABLE                                       |
| cost_per_unit_time | FLOAT     | NOT NULL                                       |

---

