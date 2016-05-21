from flask import Flask, render_template, jsonify
from random import randint


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/coisas")
def coisas():
    json_data = open("static/data/coisas.json", "r").read()
    return jsonify(coisas=json_data)


@app.route("/coisa")
def coisa_sorteada():
    coisas = {0: 'uma coisa', 1: 'outra coisa', 2: 'mais outra coisa'}
    coisa_sorteada = randint(0, 2)
    return jsonify(coisa=coisas.get(coisa_sorteada))


@app.route("/quem")
def quem():
    return render_template("quem.html")


@app.errorhandler(404)
def page_not_found(e):
    return "Esta URL nao existe o.O", 404


@app.errorhandler(500)
def application_error(e):
    return "Erro inesperado. Deve ter sido o programador antigo...".format(e), 500


if __name__ == "__main__":
    app.run()
