# Vehicle Parking Management System

A web-based system to manage urban parking efficiently with **real-time spot allocation**, **user/admin roles**, and **analytics dashboards**.  

This project was built as part of the **MAD-1 Project @ IIT Madras Bootcamp**, where I designed, coded, and demoed it live.

---

## Features
- Real-time parking spot allocation  
- User and Admin role-based access  
- Booking and reservation management  
- Parking data visualization with charts  
- Authentication (login/logout system)  

---

## Technologies Used
- **Flask (App + API):** Backend logic, routing, RESTful endpoints  
- **SQLite + SQLAlchemy:** Data modeling & persistence  
- **HTML + Jinja2:** Dynamic template rendering  
- **Bootstrap + CSS:** Responsive UI styling  
- **JavaScript:** Interactivity, form validation, dynamic dashboards  
- **Authentication:** Session-based login/logout with role differentiation  

---

## Setup Instructions

To create a virtual environment, run:

```bash
# For Linux and macOS
python3 -m venv .env
# For Windows
python -m venv .env
```

To activate the virtual environment, use the following command:

```bash
source .env/bin/activate
```

Once you have activated the virtual environment, you can install the required packages using the following command provided 'requirements.txt' is present in the same directory:

```bash
pip install -r requirements.txt
```
or you can install the packages individually:

```bash
pip install flask
pip install flask_sqlalchemy
```

To run the Flask application, use the following command:

```bash
python app.py
```
provided 'app.py' is the main file of your Flask application.

