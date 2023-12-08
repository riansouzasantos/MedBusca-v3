from medbusca import app, db
from medbusca import models
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from medbusca.forms import DisponibilidadeMedicoForm
from flask import request
from medbusca.models import Disponibilidade_medico_view  # Importando o modelo correto

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time



# Rota para exibir o formulário de busca
@app.route('/')
def hero():
    return render_template('index.html')

@app.route('/busca', methods=['POST','GET'])
def busca():
    formresultado = DisponibilidadeMedicoForm()
    
    # Busca todas as especialidades, cidades e estados disponíveis no banco de dados
    especialidades = Disponibilidade_medico_view.query.with_entities(Disponibilidade_medico_view.descricao_esp).distinct().all()
    cidades = Disponibilidade_medico_view.query.with_entities(Disponibilidade_medico_view.cidade_unidade).distinct().all()
    estados = Disponibilidade_medico_view.query.with_entities(Disponibilidade_medico_view.estado_unidade).distinct().all()
    
    # Transforma as listas de tuplas em listas simples
    lista_especialidades = [esp[0] for esp in especialidades]
    lista_cidades = [cidade[0] for cidade in cidades]
    lista_estados = [estado[0] for estado in estados]
    
    return render_template('busca.html', formresultado=formresultado, especialidades=lista_especialidades, cidades=lista_cidades, estados=lista_estados)





@app.route('/sobre', methods=['POST', 'GET'])
def sobre():
    return render_template('sobre.html')

# Rota para processar a busca
@app.route('/resultados', methods=['POST', 'GET'])
def resultados():
    formresultado = DisponibilidadeMedicoForm(request.form)
    if request.method == 'POST' and formresultado.validate():
        estado = request.form['estado_unidade']  # Captura usando os nomes dos campos no HTML
        cidade = request.form['cidade_unidade']  # Captura usando os nomes dos campos no HTML
        especialidade = request.form['especialidade']  # Captura usando os nomes dos campos no HTML

        # Modificando a consulta para buscar pela descrição da especialidade
        resultados = Disponibilidade_medico_view.query.filter(
            Disponibilidade_medico_view.estado_unidade == estado,
            Disponibilidade_medico_view.cidade_unidade == cidade,
            Disponibilidade_medico_view.descricao_esp == especialidade
        ).all()

        print(resultados)  # Verifique se há dados retornados após a consulta

        return render_template('resultados.html', resultados=resultados)

    return render_template('busca.html', formresultado=formresultado)




  

#  # imports do SELENIUM

def buscar_localizacao_google_maps(endereco):
    # Configura as opções do Chrome
    options = Options()
    # Execução sem abrir a interface gráfica
    # Assim, podemos gerar o endereço sem abrir janelas, ou seja, de forma 'silenciosa'
    options.add_argument("--headless")

    # Inicializa o serviço do ChromeDriver
    service = Service(ChromeDriverManager().install())

    # Inicializa o driver do Chrome
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.google.com.br/maps/")
        # Espera até encontrar o campo de pesquisa
        search_box = driver.find_element(By.XPATH, "//input[@autofocus='autofocus']")
        search_box.clear()
        search_box.send_keys(endereco)
        search_box.send_keys(Keys.RETURN)

        # Aguarda um tempo para carregar a página
        time.sleep(5)

        # Obtém a URL da página atual
        url = driver.current_url

    except NoSuchElementException as e:
        print("Elemento não encontrado:", e)
        url = None

    driver.quit()
    return url


@app.route('/atualiza_endurl', methods=['POST', 'GET'])
def atualizaurl():
    unidades = Disponibilidade_medico_view.query.all()
    for unidade in unidades:
        endereco = (
            unidade.rua_unidade + " " + unidade.numero_unidade + " " +
            unidade.bairro_unidade + " " + unidade.cidade_unidade + " " +
            unidade.cep_unidade + " " + unidade.estado_unidade
        )
        # Obtém o link da localização usando a função buscar_localizacao_google_maps
        endereco_url = buscar_localizacao_google_maps(endereco)
        # Atualiza o campo url_unidade na tabela Disponibilidade_medico_view com o link obtido
        unidade.url_unidade = endereco_url

    # Confirma as alterações no banco de dados fora do loop
    db.session.commit()

    return render_template('atualizar.html', unidades=unidades)
#Exibe relação de upas
#exibeupas
@app.route('/exibeupas', methods=['POST', 'GET'])
def exibeupas():
    unidades = models.Unidade.query.all()
    return render_template('atualizaurl.html', unidades=unidades)

