from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '21aceda4d8254352b47a4b407cd54c7f'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tcc'




# configurações do LIVRO
# app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/medbusca/static/uploads'
#Usar o banco já criado
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#app.config['WTF_CSRF_SECRET_KEY'] = 'random key for form'
#Melhor método



if os.getenv('DATABASE_URL'):
    # Produção - banco Postgres
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    # engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/')
else:
    banco = 'mysql'
    #banco = 'sqlite'
    if banco == 'sqlite':
        # Configuração do banco no SQLALCHEMY
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tcc.db'

    elif banco == 'mysql':
         app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tcc'

db = SQLAlchemy(app)
from medbusca import routes    