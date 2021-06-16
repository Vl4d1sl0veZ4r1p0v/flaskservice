import json
import numpy as np
from sklearn import datasets
from flask import Flask, request, abort, Response
from model import Model

app = Flask(__name__)

clf_ = Model()

BREAK_FOLDER = 'data'
ALLOWED_EXTENSIONS = ['txt']


# delete
def get_data():
    from sklearn.model_selection import train_test_split
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    return X_test, y_test


#

@app.route('/', methods=['GET'])
def start():

    return 'Make your query...'


@app.route('/classify', methods=['POST'])
def predict():
    if not (request.json and 'text' in request.json):
        abort(Response("Your request should be in JSON format: {'text':[texts]}\n"))
    user_query = request.json['text']
    #:todo
    data = list(map(float, user_query.split(' ')))
    data = np.array([data])
    try:
        prediction = clf_.predict(data)
    except Exception as ex:
        prediction = ex
    return {'prediction': prediction.tolist()}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
