import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
from tf_idf import tfidf_vectorizer
import numpy as np
from scipy import misc
import pickle

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])

def predict():
    naivebayes_model = open("previous_tfidf_matrix_train.pickle","rb")
    clf = joblib.load(naivebayes_model)
    if request.method=='POST':
        namequery = request.form['namequery']
        data = [namequery]
        vect = tfidf_vectorizer.transform(data).toarray()
        my_prediction = clf.predict(vect)
    return render_template('results.html',prediction = my_prediction,name = namequery)
        

if __name__ == '__main__':
    app.run()