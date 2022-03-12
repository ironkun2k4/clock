from flask import Flask, request, render_template

app = Flask(__name__)

events = ['2022 event 1', '2022 event 2', '2022 event 3']


@app.route('/', methods=['POST', 'GET'])
def welcome():
    if request.method == 'POST':
        # TODO: Use request.form to access form input values
        ...
    else:
        content = render_template('index.html', events=events)
        return content
