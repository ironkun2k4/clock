import flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    content = render_template('index.html')
    return content
