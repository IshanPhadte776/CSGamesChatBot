from flask import Flask
from transformers import pipeline
import requests as r
import json

API_URL = "https://xevhza5rhd1jhkq8.us-east-1.aws.endpoints.huggingface.cloud"

headers = {
	"Accept" : "application/json",
	"Content-Type": "application/json" 
}

def query(payload):
	response = r.post(API_URL, headers=headers, json=payload)
	return response.json()

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

#
@app.route('/TMP', methods=['POST'])
def hello():
    output = query({
        "inputs": "Say hello big boi",
        "parameters": {}
    })
    return output["generated_text"]