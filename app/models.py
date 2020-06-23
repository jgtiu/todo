from datetime import datetime
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(120), index=True, unique=True)
    due_date = db.Column(db.DateTime, default=datetime(2020, 6, 30))
    est_duration_hours = db.Column(db.Float, default=2) # todo: convert to int then divide by 100 later
    timestamp_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Task {}>'.format(self.task_name)