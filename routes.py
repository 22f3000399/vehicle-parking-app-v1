from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User, ParkingLot, ParkingSpot, Reservation
from app import app

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
