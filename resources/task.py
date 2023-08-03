from flask_restful import Resource
from flask import request,abort, Response
from marshmallow import fields, ValidationError
from data import ma,db
from models.job import Task, task_schema



class TaskResource(Resource):
    # get the resource given the id
    def get(self, id):
        task = Task.query.filter(Task.id == id).first()
        if not task:
            abort(404, description="Could not find that id")
        return task_schema.dump(task),200

    # Check if a resource exists.  If not create it.
    # In REST PUT can also be used to update an existing resource
    # And the URL must contain the resource id
    def put(self, id):
        task = Task.query.filter(Task.id == id).first()
        if task:
            abort(404, description="Id already exists, cannot add")
        try:
            task = task_schema.load(request.get_json(), partial=True)
            task.id = id
        except ValidationError as err:
            print(err.messages)
            abort(404, err.messages)
        db.session.add(task)
        db.session.commit()
        return task_schema.dump(task),201

    # Update an existing resource with new data
    def patch(self, id):
        task = Task.query.filter(Task.id == id).first()
        if not task:
            abort(404, message = "Id does not exist, cannot modify")
        try:
            task_update = task_schema.load(request.get_json(), partial=True)
        except ValidationError as err:
            abort(404, err.messages)
        if task_update.description:
            task.description = task_update.description
        db.session.commit()
        return task_schema.dump(task),200

    # delete an existing resource
    def delete(self,id):
        task = Task.query.filter(Task.id == id).first()
        if not task:
            abort(404, message = "id does not exist, cannot delete")
        db.session.delete(task)
        db.session.commit()
        return Response(status = 204)

    

class TaskPostResource(Resource):
    # POST is to create a new resource, whether it already exists or not.
    # the URL will not contain the resource id
    def post(self):
        try:
            task = task_schema.load(request.get_json(), partial=True)
            print('loaded')
        except ValidationError as err:
            print(err.messages)
            abort(404,err.messages)

        db.session.add(task)
        db.session.commit()
        return task_schema.dump(task), 201