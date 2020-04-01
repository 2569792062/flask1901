from flask import Flask
app = Flask(__name__)

@app.route('/')
def idnex():
    return '<h1>demo..</h1>'