# ATENÇÃO: PROGRAMA AINDA NÃO ESTÁ PRONTO!
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "API Index Page"


@app.route('/vendas')
def vendas():
    table = pd.read_csv('csv/advertising.csv')
    total_vendas = table['Vendas'].sum()
    qtd_vendas = table['Vendas'].count()
    media_vendas = table['Vendas'].mean()
    resposta = {
        "Total de Vendas": round(float(total_vendas), 2),
        "Qtd. de Vendas": float(qtd_vendas),
        "Media de Vendas": round(float(media_vendas), 2)
    }
    return jsonify(resposta)


app.run()
