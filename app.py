import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_base = "https://{}.openai.azure.com/".format(os.getenv("OPENAI_NAME"))
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")

CORS(app)

@app.route('/', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def generate_text():
    if not request.get_json().get('prompt'):
        return jsonify({'error': 'Please enter valid JSON body'}), 400
    stop = None
    if (len(json.loads(os.getenv("STOP"))) > 0):
        stop = json.loads(os.getenv("STOP"))
    prompt = os.getenv("PREPROMPT") + '\n' + request.get_json().get('prompt') + '\n\n'
    response = openai.Completion.create(
        engine=os.getenv("ENGINE"),
        prompt=prompt,
        temperature=float(os.getenv("TEMPERATURE")),
        max_tokens=int(os.getenv("MAX_TOKENS")),
        top_p=float(os.getenv("TOP_P")),
        frequency_penalty=float(os.getenv("FREQUENCY_PENALTY")),
        presence_penalty=float(os.getenv("PRESENCE_PENALTY")),
        best_of=1,
        stop=stop
    )

    return jsonify(response.choices[0].text), 200

if __name__ == '__main__':
    app.run()
