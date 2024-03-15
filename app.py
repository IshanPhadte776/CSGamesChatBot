from flask import Flask
from transformers import pipeline
import requests as r
from flask import request

app = Flask(__name__)

#loading static files
def load_file(location: str):
    with open(location, "r", encoding="utf8") as f:
        return f.read()

@app.route("/", methods=['GET'])
def index():
    return load_file("index.html")

@app.route("/style.css", methods=['GET'])
def style():
    return load_file("style.css")

@app.route("/index.js", methods=['GET'])
def js():
    return load_file("index.js")



API_URL = "https://xevhza5rhd1jhkq8.us-east-1.aws.endpoints.huggingface.cloud"

headers = {
    "Accept" : "application/json",
    "Content-Type": "application/json" ,
}

def query(payload):
    response = r.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/model_query', methods=['GET'])
def model_query():
    
    print(request.get_json())

    question = "What are the symptoms of diabetes?"
    context = "Diabetes is a metabolic disease that causes high blood sugar. The symptoms include increased thirst, frequent urination, and unexplained weight loss."
    
    query_input = f"Context: {context}\n\nQuestion: {question}\n\nAnswer: "

    output = query({
        "inputs": query_input,
        "parameters": {
            "max_new_tokens": 256,
            "temperature": 0.1,
        }
    })
    return output