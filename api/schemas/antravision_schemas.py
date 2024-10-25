from api import ma
from marshmallow import Schema, fields

class SignUpSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'nome', 'telefone', 'email', 'senha', 'endereco')
    
    _id = fields.Str()
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    email = fields.Str(required=True)
    senha = fields.Str(required=True)
    endereco = fields.Dict(required=True)

class DadosSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'plan', 'proprietario', 'telefone', 'dt_analise', 'doenca', 'observacao')
        
    _id = fields.Str()
    plan = fields.Str(required=True)
    proprietario = fields.Str(required=True)
    telefone = fields.Str(required=True)
    dt_analise = fields.Date(required=True)
    doenca = fields.Str(required=True)
    observacao = fields.Str(required=True)    