from flask_restful import Resource
from api import api
from flask import make_response,jsonify, request
from ..schemas import antravision_schema
from ..models import antravision_model
from ..services.antravision_service import AntravisionService

class AntravisionList(Resource):
    def get(self):
        