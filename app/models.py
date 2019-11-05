from app import db

class Events(db.Model):
    eventID=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date)
    title=db.Column(db.String(250))
    description=db.Column(db.String(250))
    isCompleted=db.Column(db.Boolean, default=False)