from flask import Flask
from transformers import pipeline
import requests as r
from flask import request, session

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

@app.route('/model_query', methods=['POST'])
def model_query():

    print("Model query")
    
    data = request.get_json()

    print(data)


    user_query = data["query"]
    short_term_memory = "\n".join(data["buf"])
    
    query_input = f"{short_term_memory}\n\npatient:{user_query}\n\nAnswer the query as a medical professional: "

    output = query({
        "inputs": query_input,
        "parameters": {
            "max_new_tokens": 256,
            "temperature": 0.1,
        }
    })
    return output


##

# {
#     "buf": ["user:I have a bloody nose", "bot:How can we aid you?", "bot:Hello"],
#     "query":"I have a bloody nose"
# }