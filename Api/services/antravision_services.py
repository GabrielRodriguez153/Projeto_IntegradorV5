from Api import mongo
from flask import render_template
from ..models import antravision_model
from bson import ObjectId 
from datetime import datetime

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
    
    notifications_cache = []
    
    @staticmethod
    def save_notification(message):
        DadosService.notifications_cache.append({"message": message, "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")})

    @staticmethod
    def get_notifications():
        return DadosService.notifications_cache

    @staticmethod
    def clear_notifications():
        DadosService.notifications_cache = []
    
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
            
            result = list(mongo.db.dados.aggregate([
                {
                    "$addFields": {
                        "hectares_numeric": {
                            "$toInt": "$hectares"  
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
            result = list(mongo.db.dados.aggregate([
                {"$group": {"_id": "$nivelInfestacao", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
            ]))
            return result[0]['_id'] if result else "N/A"
        except Exception as e:
            print(f"Erro ao obter o nível de severidade mais frequente: {str(e)}")
            return "N/A"
        
    @staticmethod
    def get_dados_grafico():
        try:
            result = list(mongo.db.dados.aggregate([
                {"$group": {"_id": "$localizacao", "totalPlantacoes": {"$sum": 1}}},
                {"$sort": {"totalPlantacoes": -1}}
            ]))

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
        
        if updated_dado:
            mensagem = f"Histórico atualizado: {updated_dado.get('proprietario', 'Proprietário desconhecido')} - " \
                   f"Status: {updated_data.get('status', 'N/A')}."
        DadosService.notifications_cache.append({
            "message": mensagem,
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
            
        return updated_dado

    @staticmethod
    def delete_dado(dado_id):
        mongo.db.dados.delete_one({'_id': ObjectId(dado_id)})

