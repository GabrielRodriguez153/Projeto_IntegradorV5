from api import app, mongo
from api.models.antravision_model import SignUp, Dados
from api.services.antravision_services import SignUpService, DadosService
from bson import datetime as bson_datetime

if __name__ == '__main__':
    with app.app_context():
        if 'signup' not in mongo.db.list_collection_names():
            signup = SignUp(
                nome = '',
                telefone = '',
                email = '',
                senha = '',
                endereco = ''
            )
            SignUpService.add_user(signup)
        
        if 'dados' not in mongo.db.list_collection_names():
            dado = Dados(
                plan = '',
                proprietario = '',
                telefone = '',
                dt_analise = bson_datetime.datetime.utcnow(),
                doenca = '',
                observacao = '' 
            )
            DadosService.add_dado(dado)
    app.run(port=4000, debug=True)