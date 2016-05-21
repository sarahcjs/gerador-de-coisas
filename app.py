from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/coisas")
def coisas():
    return jsonify({"name": "Minha Coisa"})


@app.route("/quem")
def index():
    return render_template("quem.html")

if __name__ == "__main__":
    app.run()
