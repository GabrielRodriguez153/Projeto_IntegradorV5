from Api import mongo

class SignUp():
    def __init__(self, nome,telefone,email,senha,endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email 
        self.senha = senha
        self.endereco = endereco

class Dados():
    def __init__(self, localizacao, nivelInfestacao, status, dataDeteccao, proprietario, observacoes, hectares=0):
        self.localizacao = localizacao
        self.nivelInfestacao = nivelInfestacao
        self.status = status
        self.dataDeteccao = dataDeteccao
        self.proprietario = proprietario
        self.observacoes = observacoes
        self.hectares = hectares
