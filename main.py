import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai

load_dotenv()


app = Flask(__name__)
CORS(app)

openai.api_key =  os.environ.get('OPEN_AI_API_KEY')

@app.route('/', methods=['GET'])
def home():
   return jsonify({'message': 'Hello World'})

@app.route('/api/openai', methods=['POST'])
def openai_api():
    data = request.get_json()
    prompt = data['prompt']
   
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return jsonify({'response': response.choices[0].text.strip()})




if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
