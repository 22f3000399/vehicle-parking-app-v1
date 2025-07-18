from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import app
import config

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    reservations = db.relationship('Reservation', backref='user', lazy=True)

class ParkingLot(db.Model):
    __tablename__ = 'parkinglots'

    id = db.Column(db.Integer, primary_key=True)
    prime_location_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    pin_code = db.Column(db.String, nullable=False)
    price_per_unit_time = db.Column(db.Float, nullable=False)
    maximum_number_of_spots = db.Column(db.Integer, nullable=False)

    spots = db.relationship('ParkingSpot', backref='lot', lazy=True)

class ParkingSpot(db.Model):
    __tablename__ = 'parkingspots'

    id = db.Column(db.Integer, primary_key=True)
    lot_id = db.Column(db.Integer, db.ForeignKey('parkinglots.id'), nullable=False)
    status = db.Column(db.String(1), default='A', nullable=False)

    __table_args__ = (
        db.CheckConstraint(status.in_(['A', 'O']), name='check_spot_status'),
    )

    reservations = db.relationship('Reservation', backref='spot', lazy=True)

class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    spot_id = db.Column(db.Integer, db.ForeignKey('parkingspots.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    parking_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    leaving_timestamp = db.Column(db.DateTime, nullable=True)
    cost_per_unit_time = db.Column(db.Float, nullable=False)




