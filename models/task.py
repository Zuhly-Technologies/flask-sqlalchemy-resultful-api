from data import db, ma
from .job import *
from datetime import datetime
from marshmallow import fields

#A Job can have multiple tasks associated with it, this can represent the 1 to Many Relationship
class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=True)

    def __repr__(self):
        return f"Task(description={self.description})"


class TaskSchema(ma.SQLAlchemyAutoSchema):
    job_id = fields.Integer()
    class Meta:
        model = Task
        load_instance = True

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)