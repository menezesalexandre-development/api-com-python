# ATENÇÃO: PROGRAMA AINDA NÃO ESTÁ PRONTO!
import pandas as pd
from flask import Flask, jsonify

<<<<<<< Updated upstream
app = Flask(__name__)

@app.route('/')
def index(): 
  return "API Index Page" 

@app.route('/vendas')
def vendas():
  table = pd.read_csv('advertising.csv')
  total_vendas = table['Vendas'].sum()
  qtd_vendas = table['Vendas'].count()
  media_vendas = table['Vendas'].mean()
  resposta = {'Total de Vendas': total_vendas, 
              'Quantidade de Vendas': qtd_vendas, 
              'Média de Vendas': media_vendas}
  return jsonify(resposta)


app.run(host='0.0.0.0')
=======

>>>>>>> Stashed changes
