import sqlite3
import logging
import requests
import json

from flask import Flask, request, g

import constants

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(threadName)-9s %(message)s')

DATABASE = './sample.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_context(sentence):
    cur = get_db().cursor()
    try:
        res = cur.execute(f"""
            SELECT keyword, context
            FROM context
            WHERE '{sentence}' LIKE '%' || keyword || '%';""")
    except sqlite3.Error as e:
        logging.error(e)
        return None

    context = res.fetchone()
    if not context:
        logging.error(f'chat: no context found for {question}')
        return "error: no valid context found"

    return context

def create_chat_completion(context, question):
    # keyword = context[0], context = context[1]
    url = "https://api.openai.com/v1/chat/completions"
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
            "role": "system",
            "content": f"{context[1]}"
            },
            {
            "role": "user",
            "content": f"{question}"
            }
        ]
        })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {constants.APIKEY}'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except requests.exceptions.RequestException as e:
        logging.error(e)
        return None

    if response.status_code != 200:
        logging.error(f'create_chat_completion: status_code={response.status_code}, text={response.text}')
        return None

    return response.json()['choices'][0]['message']['content']

@app.route("/")
def hello():
    return "<p>chatbot 1.0!</p>"

@app.post("/chat")
def chat():
    question = request.json['prompt']

    # grab the context from the database
    context = get_context(question)


    # send prompt and context to openai
    answer = create_chat_completion(context, question)

    return answer

@app.teardown_appcontext
def close_connection(exception):
    """Closes the database again at the end of the request."""

    logging.debug(f'close_connection: exception={exception}')
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()