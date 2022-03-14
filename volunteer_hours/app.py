from flask import Flask, request, render_template

app = Flask(__name__)

events = ['2022 event 1', '2022 event 2', '2022 event 3']


@app.route('/', methods=['POST', 'GET'])
def main_screen():
    """
    Define the main screen
    """
    if request.method == 'POST':
        # Use request.form to access form input values
        # Go to new page with response data
        ...
    content = render_template('index.html', events=events)
    return content
