from Api import ma
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
        fields = ('_id', 'localizacao', 'nivelInfestacao', 'status', 'dataDeteccao', 'proprietario', 'observacoes', 'hectares')
        
    _id = fields.Str()
    localizacao = fields.Str(required=True)
    nivelInfestacao = fields.Str(required=True)
    status = fields.Str(required=True)
    dataDeteccao = fields.Str(required=True)
    proprietario = fields.Str(required=True)
    observacoes = fields.Str(required=True)  
    hectares = fields.Str(required=True)  