import flask
from flask import Flask, jsonify, request, render_template
import json
import pickle
import numpy as np


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

@app.route('/result', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form.to_dict()
        data = list(data.values())
        data = np.array(list(map(np.float,data)))
        model = load_models()
        result = model.predict(data.reshape(1,-1))[0]
    
        
    return render_template("result.html", prediction=result)



if __name__ == '__main__':
    application.run(debug=True)