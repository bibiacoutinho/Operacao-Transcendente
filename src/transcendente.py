from flask import Flask
from flask import render_template
from flask import request
import math
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/seno', methods=['POST'])
def seno():
  n1 = float(request.form.get('n1'))
  n1 = math.radians(n1)
  seno = math.sin(n1)
  return str(seno)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5003)
