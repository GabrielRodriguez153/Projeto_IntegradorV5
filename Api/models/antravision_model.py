from Api import mongo

class SignUp():
    def __init__(self, nome,telefone,email,senha,endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email 
        self.senha = senha
        self.endereco = endereco

class Dados():
    def __init__(self, localizacao, infestacao, status, dt_analise, proprietario, observacao):
        self.localizacao = localizacao
        self.infestacao = infestacao
        self.status = status
        self.dt_analise = dt_analise
        self.proprietario = proprietario
        self.observacao = observacao