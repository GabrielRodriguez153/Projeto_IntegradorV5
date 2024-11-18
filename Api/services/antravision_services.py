from Api import mongo
from ..models import antravision_model
from bson import ObjectId 

class SignUpService:
    
    @staticmethod
    def add_user(user):
        user['endereco'] = {}
        result = mongo.db.signup.insert_one(user)
        return mongo.db.signup.find_one({'_id': ObjectId(result.inserted_id)})
    
    @staticmethod
    def get_user():
        return list(mongo.db.signup.find())
    
    @staticmethod
    def get_user_by_id(id):
        return mongo.db.signup.find_one({'_id': ObjectId(id)})
    
    def update_user(user_id, updated_data):
        updated_user = mongo.db.signup.find_one_and_update(
            {'_id': ObjectId(user_id)},
            {'$set' : updated_data},
            return_document=True
        )
        return updated_user
    
    @staticmethod
    def validate_login(email, senha):
        user = mongo.db.signup.find_one({'email': email, 'senha': senha})
        return user
    
    @staticmethod
    def delete_user(id):
        mongo.db.signup.delete_one({'_id':ObjectId(id)})

class DadosService:
    @staticmethod
    def add_dado(data):
        result = mongo.db.dados.insert_one(data)
        return mongo.db.dados.find_one({'_id': ObjectId(result.inserted_id)})

    @staticmethod
    def get_dado():
        return list(mongo.db.dados.find())

    @staticmethod
    def get_dado_by_id(dado_id):
        return mongo.db.dados.find_one({'_id': ObjectId(dado_id)})

    @staticmethod
    def update_dado(dado_id, updated_data):
        updated_dado = mongo.db.dados.find_one_and_update(
            {'_id': ObjectId(dado_id)},
            {'$set': updated_data},
            return_document=True
        )
        return updated_dado

    @staticmethod
    def delete_dado(dado_id):
        mongo.db.dados.delete_one({'_id': ObjectId(dado_id)})