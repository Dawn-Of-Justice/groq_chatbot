from flask import render_template, request
from flask_app import app
from flask_app.utils import beutify
from groq_chatbot.groq_chatbot import DocumentResponder

doc = "data\Corpus.pdf"
doc_responder = DocumentResponder(doc)

@app.route("/")
def index():
    return render_template('chat.html', doc_name=beutify(doc))

@app.route("/get", methods=["GET", "POST"])
def chat():
    user_query = request.form["msg"]
    history = ''
    result = doc_responder.response(user_query, history)
    return result
