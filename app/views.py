from flask import Flask, render_template, jsonify, request

from grandpy.grandpy import answer as grandpy_answer

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html", title="Grandpy", page_title="Bienvenue sur mon exemple"
    )


@app.route("/answer", methods=["POST"])
def answer():
    question = request.form["question"]
    response = grandpy_answer(question)
    return jsonify(response)
