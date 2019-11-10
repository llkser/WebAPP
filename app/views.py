from flask import render_template, flash, redirect, session, url_for, request, g
from sqlalchemy import *
from app import app, db, models
from .models import Events

from .forms import EventsForm

@app.route("/" , methods=['GET'])
def getAllEvents():
    EventsTable=Events.query.order_by('date').all()
    return render_template('index.html',
                            EventsTable=EventsTable,
                            )

@app.route('/edit_event/<id>', methods=['GET','POST'])
def edit_event(id):
    event=Events.query.get(id)
    form = EventsForm(obj=event)
    if form.validate_on_submit():
        event.date=form.date.data
        event.title=form.title.data
        event.description=form.description.data
        db.session.commit()
        return redirect('/')

    return render_template('edit_event.html',
                           form=form)

@app.route('/add_event', methods=['GET','POST'])
def add_event():
    form=EventsForm()
    if form.validate_on_submit():
        maxID = Events.query.order_by(desc('eventID')).first().eventID
        print(maxID)
        t = Events(eventID=maxID+1, 
            date=form.date.data, 
            title=form.title.data, 
            description=form.description.data, 
            isCompleted=False)
        db.session.add(t)
        db.session.commit()
        return redirect('/')

    return render_template('add_event.html',
                           form=form)

@app.route('/change_event_status/<id>', methods=['GET'])
def change_event_status(id):
    event=Events.query.get(id)
    event.isCompleted=not event.isCompleted
    db.session.commit()
    return redirect('/')

@app.route('/delete_event/<id>', methods=['GET'])
def delete_event(id):
    event=Events.query.get(id)
    db.session.delete(event)
    db.session.commit()
    return redirect('/')

@app.route('/viewCompleted', methods=['GET'])
def viewCompleted():
    EventsTable=Events.query.order_by('date').all()
    return render_template('view_completed.html',
                            EventsTable=EventsTable,
                            )

@app.route('/viewUncompleted', methods=['GET'])
def viewUncompleted():
    EventsTable=Events.query.order_by('date').all()
    return render_template('view_uncompleted.html',
                            EventsTable=EventsTable,
                            )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404