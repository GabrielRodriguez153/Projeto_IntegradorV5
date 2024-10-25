from api import mongo

class SignUp():
    def __init__(self, nome,telefone,email,senha,endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.endereco = endereco

class Dados():
    def __init__(self, plan, proprietario, telefone, dt_analise, doenca, observacao):
        self.plan = plan
        self.proprietario = proprietario
        self.telefone = telefone
        self.dt_analise = dt_analise
        self.doenca = doenca
        self.observacao = observacao