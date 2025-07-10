# Vehicle Parking App - V1

## Overview
This is a multi-user vehicle parking management application built with **Flask** (backend), **Jinja2, HTML, CSS, Bootstrap** (frontend), and **SQLite** (database). The app supports two roles:

- **Admin (Superuser):** Manages parking lots, parking spots, and monitors parking statuses.
- **User:** Registers, logs in, and reserves parking spots automatically assigned by the app.

## Features

### Admin
- Superuser with no registration required (pre-created in the database).
- Create, edit, and delete parking lots.
- Each parking lot has multiple parking spots generated automatically based on the maximum capacity.
- View status of all parking spots and details of occupied spots.
- View all registered users and summary charts of parking lots and spots.

### User
- Register and login functionality.
- Choose an available parking lot.
- Book the first available parking spot automatically.
- Release/vacate the parking spot.
- View parking history and summary charts.

## Technologies Used
- **Backend:** Flask
- **Frontend:** Jinja2 templates, HTML, CSS, Bootstrap
- **Database:** SQLite (created programmatically, no manual DB setup)
