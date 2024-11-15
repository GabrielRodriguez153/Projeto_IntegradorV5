from flask_restful import Resource
from api import api
from flask import make_response,jsonify, request
from api.schemas import antravision_schemas
from api.models import antravision_model
from api.services.antravision_services import SignUpService, DadosService

class SignUpList(Resource):
    def get(self):
        users = SignUpService.get_user()
        user = antravision_schemas.SignUpSchema(many=True)
        return make_response(user.jsonify(users), 200)
    
    def post(self):
        userschema = antravision_schemas.SignUpSchema()
        validate = userschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_user = antravision_model.SignUp(**json_data)
            result = SignUpService.add_user(new_user)
            res = userschema.jsonify(result)
            return make_response(res,201)
        
class SignUpDetails(Resource):
    def get(self, id):
        user = SignUpService.get_user_by_id(id)
        if user is None:
            return make_response(jsonify("Usuário não Encontrado"), 400)
        userschema = antravision_schemas.SignUpSchema()
        return make_response(userschema.jsonify(user), 200)
    
    def put(self, id):
        user_bd = SignUpService.get_user_by_id(id)
        if user_bd is None:
            return make_response(jsonify("Usuário não Encontrado"), 404)
        userschema = antravision_schemas.SignUpSchema()
        validate = userschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else: 
            json_data = request.get_json()
            new_user = antravision_model.SignUp(**json_data)        
            updated_user = SignUpService.update_user(new_user,id)
            return make_response(userschema.jsonify(updated_user), 200)
    
    def delete(self, id):
        user_bd = SignUpService.get_user_by_id(id)
        if user_bd is None:
            return make_response(jsonify("Usuário não Encontrado"), 404)
        SignUpService.delete_user(id)
        return make_response(jsonify("Usuário Excluído com Sucesso!"), 200)

class DadosList(Resource):
    def get(self):
        dados = DadosService.get_dado()
        dado = antravision_schemas.DadosSchema(many=True)
        return make_response(dado.jsonify(dados), 200)
    
    def post(self):
        dadoschema = antravision_schemas.DadosSchema()
        validate = dadoschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_dado = antravision_model.Dados(**json_data)
            result = DadosService.add_dado(new_dado)
            res = dadoschema.jsonify(result)
            return make_response(res,201)

class DadosDetails(Resource):
    def get(self, id):
        dado = DadosService.get_dado_by_id(id)
        if dado is None:
            return make_response(jsonify("Dados não Encontrados"), 400)
        dadoschema = antravision_schemas.DadosSchema()
        return make_response(dadoschema.jsonify(dado), 200)
    
    def put(self, id):
        dado_bd = DadosService.get_dado_by_id(id)
        if dado_bd is None:
            return make_response(jsonify("Dados não Encontrados"), 404)
        dadoschema = antravision_schemas.DadosSchema()
        validate = dadoschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            if '_id' in json_data:
                del json_data['_id']
            new_dado = antravision_model.Dados(**json_data)
            updated_dado = DadosService.update_dado(new_dado,id)
            return make_response(dadoschema.jsonify(updated_dado), 200)
    
    def delete(self, id):
        dado_bd = DadosService.get_dado_by_id(id)
        if dado_bd is None:
            return make_response(jsonify("Dados não Encontrados"), 404)
        DadosService.delete_dado(id)
        return make_response(jsonify("Dados Excluídos com Sucesso!"), 200)
        
api.add_resource(SignUpList, '/users')
api.add_resource(SignUpDetails, '/user/<id>')
api.add_resource(DadosList, '/dados')
api.add_resource(DadosDetails, '/dado/<id>')