import flask
from flask import Flask, render_template

app = Flask(__name__)

events = ['2022 event 1', '2022 event 2', '2022 event 3']


@app.route('/')
def welcome():
    content = render_template('index.html', events=events)
    return content
