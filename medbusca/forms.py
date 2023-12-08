from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DateTimeField, IntegerField
from wtforms.validators import DataRequired


class DisponibilidadeMedicoForm(FlaskForm):
    estado_unidade = StringField('Estado:')
    cidade_unidade = StringField('Cidade:')
    especialidade = StringField('Especialidade:')