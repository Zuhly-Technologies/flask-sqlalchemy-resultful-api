from data import db, ma
from datetime import datetime

class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime, nullable = False)
    status = db.Column(db.String(10), nullable = False)

    tasks = db.relationship('Task', backref='job', lazy=True)

    def __repr__(self):
        return f"Job(name = {name}, created_at = {created_at}, status= {status})"
    
#A Job can have multiple tasks associated with it, this can represent the 1 to Many Relationship
class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=True)

    def __repr__(self):
        return f"Task(description={description})"


class JobSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Job
        load_instance = True


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True

job_schema = JobSchema()
jobs_schema = JobSchema(many=True)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

