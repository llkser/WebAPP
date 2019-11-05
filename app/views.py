from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, models
from .models import Events

from .forms import EventsForm

@app.route("/" , methods=['GET'])
def getAllEvents():
    EventsTable=Events.query.all()
    return render_template('index.html',
                            EventsTable=EventsTable,
                            )