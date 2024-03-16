from flask import Flask
from transformers import pipeline
import requests as r
from flask import request, session
from typing import List, Optional
import re

app = Flask(__name__)

# SECRET KEY FROM FLASK DOCS - IT IS NOT SECRET OR SECURE ;)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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

# API stuff
API_URL = "https://xevhza5rhd1jhkq8.us-east-1.aws.endpoints.huggingface.cloud"

headers = {
    "Accept" : "application/json",
    "Content-Type": "application/json" ,
}

def query(payload):
    response = r.post(API_URL, headers=headers, json=payload)

<<<<<<< HEAD
@app.route('/model_query', methods=['POST'])
def model_query():

    print("Model query")
    
    data = request.get_json()

    print(data)



    user_query = data["query"]
    short_term_memory = "\n".join(data["buf"])

<<<<<<< HEAD
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
=======
    # what do we do???
    action = None
    match (session["model_state"], session["model_sub_state"]):
        case ("GATHER", _):
            action = zsc(user_query, ["symptom"]) if not None else "INVALID RESPONSE"
        case (_, _):
            session["model_state"] = "GATHER"
            session["model_sub_state"] = "None"

    match action:
        case "symptom":
            if "symptoms" not in session:
                session["symptoms"] = []
            session["symptoms"].append(extract_symptom(user_query))
            query_input = f"Chat log: {short_term_memory}\n\npatient:{user_query}\n\nTell the patient you have documented the symptom and ask for more symptoms or details or to get diagnosis: "
            output = query({
                "inputs": query_input,
                "parameters": {
                    "max_new_tokens": 64,
                    "length_penalty": 24.,
                    "temperature": 0.1,
                }
            })
            return output
        case _:
            if "symptoms" in session:
                s = ", ".join(session["session"])

                query_input = f"Symptoms: {s}\nDiagnose the patient using the listed symptons"
                output = query({
                    "inputs": query_input,
                    "parameters": {
                        "max_new_tokens": 356,
                        "length_penalty": 24.,
                        "temperature": 4.0,
                    }
                })
                return output
            else:
                query_input = f"Chat log: {short_term_memory}\n\npatient:{user_query}\n\nAnswer the chat like a medical professional: "

                output = query({
                    "inputs": query_input,
                    "parameters": {
                        "max_new_tokens": 64,
                        "length_penalty": 24.,
                        "temperature": 0.1,
                    }
                })
                return output
>>>>>>> 374f140a2aa55220055c9dc8befc8ede2869c1e7
