from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '21aceda4d8254352b47a4b407cd54c7f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tcc'

db = SQLAlchemy(app)

from medbusca import routes