from data import db, ma
from .task import *
from datetime import datetime
from typing import List

class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = True)
    created_at = db.Column(db.DateTime, nullable = True)
    status = db.Column(db.String(10), nullable = True)

    tasks = db.relationship('Task', backref='job', lazy=True)

    def __repr__(self):
        return f"Job(name = {self.name}, created_at = {self.created_at}, status= {self.status})"


class JobSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Job
        load_instance = True

job_schema = JobSchema()
jobs_schema = JobSchema(many=True)


