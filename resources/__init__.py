from resources.job import JobResource, JobPostResource
from resources.task import TaskResource, TaskPostResource

def add_resource(api):
    api.add_resource(JobResource, "/job/<int:id>")
    api.add_resource(JobPostResource, "/job")
    api.add_resource(TaskResource, "/task/<int:id>")
    api.add_resource(TaskPostResource, "/task")