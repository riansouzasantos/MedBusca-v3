from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '21aceda4d8254352b47a4b407cd54c7f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tcc'


db = SQLAlchemy(app)


# Rota para exibir o formulário de busca
@app.route('/')
def busca():
    return render_template('busca.html')

# Rota para processar a busca
@app.route('/resultados', methods=['POST'])
def resultados():
    estado = request.form['estado']
    cidade = request.form['cidade']
    especialidade = request.form['especialidade']

    # Consulta para buscar os dados da view filtrados
    consulta = text(f"""
        SELECT *
        FROM disponibilidade_medico_view
        WHERE estado_unidade = '{estado}'
        AND cidade_unidade = '{cidade}'
        AND especialidade = '{especialidade}'
    """)
    
    resultados = db.session.execute(consulta)

    return render_template('resultados.html', resultados=resultados)
if __name__ == '__main__':
    app.run(debug=True)
