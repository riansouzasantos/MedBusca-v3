from medbusca import db

class Disponibilidade_medico_view(db.Model):
    __tablename__ = 'disponibilidade_medico_view'

    crm_medico = db.Column(db.String, primary_key=True)
    dataHoraInicio = db.Column(db.String, primary_key=True)
    nome_unidade = db.Column(db.String, primary_key=True)
    dataHoraFim = db.Column(db.String)
    id_especialidade_m = db.Column(db.String)
    descricao_esp = db.Column(db.String)
    rua_unidade = db.Column(db.String)
    cep_unidade = db.Column(db.String)
    numero_unidade = db.Column(db.String)
    bairro_unidade = db.Column(db.String)
    cidade_unidade = db.Column(db.String)
    estado_unidade = db.Column(db.String)
    url_unidade = db.Column(db.String(250))
