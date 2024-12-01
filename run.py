from Api import mongo
from Api import app
from Web import routes

from Api.models.antravision_model import SignUp, Dados
from Api.services.antravision_services import SignUpService, DadosService


routes.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        if 'signup' not in mongo.db.list_collection_names():
            signup = SignUp(
                nome='',
                telefone='',
                email='',
                senha='',
                endereco=''
            )
            SignUpService.add_user(signup)
        
        if 'dados' not in mongo.db.list_collection_names():
            dado = Dados(
                localizacao='',
                proprietario='',
                nivelInfestacao='',
                dataDeteccao='',
                status='',
                observacoes='',
                hectares=0
            )
            DadosService.add_dado(dado)
    
    app.run(port=4000, debug=True)
