from Api import mongo
from flask import render_template
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
    def get_casos_recentes():
        try:
            total_documentos = mongo.db.dados.count_documents({})
            return total_documentos
        except Exception as e:
            print(f"Erro ao obter casos recentes: {str(e)}")
            return 0
    
    @staticmethod
    def get_hectares_afetados():
        try:
            # Soma o total de hectares afetados, convertendo o campo 'hectares' para float
            result = list(mongo.db.dados.aggregate([
                {
                    "$addFields": {
                        "hectares_numeric": {
                            "$toInt": "$hectares"  # Converte o campo 'hectares' de string para número
                        }
                    }
                },
                {
                    "$group": {
                        "_id": None,
                        "total": {"$sum": "$hectares_numeric"}
                    }
                }
            ]))
            
        
            if result and 'total' in result[0]:
                return result[0]['total']
            else:
                return 0
        except Exception as e:
            print(f"Erro ao obter hectares afetados: {str(e)}")
            return 0


    @staticmethod
    def get_nivel_severidade_mais_frequente():
        try:
            # Obtém o nível de infestação mais frequente
            result = list(mongo.db.dados.aggregate([
                {"$group": {"_id": "$nivelInfestacao", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
                {"$limit": 1}
            ]))
            return result[0]['_id'] if result else "N/A"
        except Exception as e:
            print(f"Erro ao obter o nível de severidade mais frequente: {str(e)}")
            return "N/A"
        
    @staticmethod
    def get_dados_grafico():
        try:
            # Agrupa os dados por localização e conta o número de plantações
            result = list(mongo.db.dados.aggregate([
                {"$group": {"_id": "$localizacao", "totalPlantacoes": {"$sum": 1}}},
                {"$sort": {"totalPlantacoes": -1}}
            ]))
            print(result)  # Verifique o formato dos resultados
            return result
        except Exception as e:
            print(f"Erro ao obter dados para o gráfico: {str(e)}")
            return []
    
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

