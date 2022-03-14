from flask import Flask, request, render_template

from volunteer_hours.api.ragic import Ragic

app = Flask(__name__)


def get_events() -> list[str]:
    events = Ragic().fetch_events('LYN1701685')
    names = [event['Opportunity'] for event in events.values()]
    return names


@app.route('/', methods=['POST', 'GET'])
def main_screen():
    """
    Define the main screen
    """
    if request.method == 'POST':
        # Use request.form to access form input values
        # Go to new page with response data
        ...
    events = get_events()
    content = render_template('index.html', events=events)
    return content
