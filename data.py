from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
ma = Marshmallow()

def initialize(app):
    db.init_app(app)
    ma.init_app(app)

    

