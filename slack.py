# sample usage
# export FLASK_APP=slack.py
# python -m flask run

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
  # yep, not safe ;)
  #url = 'https://hooks.slack.com/services/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'
  #payload = {'text': 'no siema!'}
  #r = requests.post(url, data=json.dumps(payload))

  data = request.json
  # verification
  if 'challenge' in data
    return jsonify({'challenge': data['challenge']})

  response = jsonify({'status': 'ok'})
  return response
