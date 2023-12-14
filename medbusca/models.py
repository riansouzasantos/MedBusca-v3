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

class Especialidade_m(db.Model):
    __tablename__ = 'especialidade_m'
    id_especialidade_m = db.Column(db.Integer, primary_key=True)
    descricao_esp = db.Column(db.String(100), nullable=False)
    def _init_(self,id_especialidade_m ,descricao_esp ):
        self.id_especialidade_m =id_especialidade_m
        self.descricao_esp = descricao_esp


class Unidades_por_especialidade_view(db.Model):
    id_unidade = db.Column(db.Integer, primary_key=True)
    id_especialidade_m = db.Column(db.Integer)
    rua_unidade = db.Column(db.String)
    cep_unidade = db.Column(db.String)
    numero_unidade = db.Column(db.String)
    bairro_unidade = db.Column(db.String)
    cidade_unidade = db.Column(db.String)
    estado_unidade = db.Column(db.String)
    nome_unidade = db.Column(db.String)
    url_unidade = db.Column(db.String)

    def _init_(self,id_unidade,id_especialidade_m, rua_unidade, cep_unidade, numero_unidade, bairro_unidade, cidade_unidade, estado_unidade, nome_unidade,  url_unidade ):
        self.id_unidade = id_unidade
        self.id_especialidade_m = id_especialidade_m
        self.rua_unidade = rua_unidade
        self.cep_unidade = cep_unidade
        self.numero_unidade = numero_unidade
        self.bairro_unidade = bairro_unidade
        self.cidade_unidade = cidade_unidade
        self.estado_unidade = estado_unidade
        self.nome_unidade = nome_unidade
        self.url_unidade = url_unidade




class Gestor(db.Model):
    __tablename__ = 'gestor'

    cpf = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(45), nullable=False)
    adm = db.Column(db.Boolean, default=False)   # Certifique-se de que os administradores têm adm=1




class ReceberInfo(db.Model):
    __tablename__ = 'receberinfo'

    id_unidade = db.Column(db.String(45), primary_key=True)
    crm_medico = db.Column(db.String(11), primary_key=True)
    dataHoraInicio = db.Column(db.DateTime, primary_key=True)
    dataHoraFim = db.Column(db.DateTime)
    id_especialidade_m = db.Column(db.Integer)
    descricao_esp = db.Column(db.String(255))
    rua_unidade = db.Column(db.String(70))
    cep_unidade = db.Column(db.String(70))
    numero_unidade = db.Column(db.String(70))
    bairro_unidade = db.Column(db.String(70))
    cidade_unidade = db.Column(db.String(70))
    estado_unidade = db.Column(db.String(70))
    nome_unidade = db.Column(db.String(70))
    url_unidade = db.Column(db.String(250))