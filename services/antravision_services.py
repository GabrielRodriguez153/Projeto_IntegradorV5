from api import mongo
from ..models import antravision_model
from bson import ObjectId

class SignUpService:
    def add_user(user):
        result = mongo.db.signup.insert_one({
             'nome' : user.nome,
             'telefone' : user.telefone,
             'email': user.email,
             'senha': user.senha,
             'endereco' : user.endereco   
        })
        return mongo.db.signup.find_one({'_id': ObjectId(result.inserted_id)})
    
    @staticmethod
    def get_user():
        return list(mongo.db.signup.find())
    
    @staticmethod
    def get_user_by_id(id):
        return mongo.db.signup.find_one({'_id': ObjectId(id)})
    
    def update_user(self, id):
        updated_user = mongo.db.signup.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set' : {
                'nome':self.nome,
                'telefone': self.telefone,
                'email': self.email,
                'senha': self.senha,
                'endereco': self.endereco
            }},
            return_document=True
        )
    @staticmethod
    def delete_user(id):
        mongo.db.signup.delete_one({'_id':ObjectId(id)})

class DadosService:
    def add_dado(dat):
        result = mongo.db.dados.insert_one({
             'plan' : dat.plan,
             'proprietario' : dat.proprietario,
             'telefone': dat.telefone,
             'dt_analise': dat.dt_analise,
             'doenca' : dat.doenca,
             'observacao' : dat.observacao   
        })
        return mongo.db.dados.find_one({'_id': ObjectId(result.inserted_id)})
    
    @staticmethod
    def get_dado():
        return list(mongo.db.dados.find())
    
    @staticmethod
    def get_dado_by_id(id):
        return mongo.db.dados.find_one({'_id': ObjectId(id)})
    
    def update_dado(self, id):
        updated_dado = mongo.db.dados.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set' : {
                'plan':self.plan,
                'proprietario': self.proprietario,
                'telefone': self.telefone,
                'dt_analise': self.dt_analise,
                'doenca': self.doenca,
                'observacao': self.observacao
            }},
            return_document=True
        )
    @staticmethod
    def delete_dado(id):
        mongo.db.dados.delete_one({'_id':ObjectId(id)})