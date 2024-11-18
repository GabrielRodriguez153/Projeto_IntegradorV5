from flask_restful import Api
from flask_pymongo import PyMongo
from flask import Flask
from flask_marshmallow import Marshmallow
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, '..', 'Web', 'views'),
    static_folder=os.path.join(BASE_DIR, '..', 'Web', 'static')
)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/antravision'
app.secret_key = '12#34$56'

api = Api(app)
mongo = PyMongo(app)
ma = Marshmallow(app)

from .resources import antravision_resources




