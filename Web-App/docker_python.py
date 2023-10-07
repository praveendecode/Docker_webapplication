import flask

from flask import Flask

import os

app  = Flask(__name__)

@app.route('/',methods=['GET'])

def home():
    return "Hello Tech Geeks This is Praveen"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='5000')


# docker build -t praveen-app

# docker push praveendecode/web-app:latest   --> push docker repo