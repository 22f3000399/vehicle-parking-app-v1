from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user

app = Flask(__name__)

import config
import models
import routes

@app.context_processor
def inject_user():
    return dict(current_user=current_user)
