import sys

from flask import Flask, request, render_template, make_response

from volunteer_hours.api.ragic import Ragic

app = Flask(__name__)


def get_events(member_id) -> list[str]:
    events = Ragic().fetch_events(member_id)
    names = [event['Opportunity'] for event in events.values()]
    return names


@app.route('/')
def main_screen():
    """
    Define the main screen
    """
    content = render_template('index.html')
    return content


@app.route('/action', methods=['GET', 'POST'])
def action_screen():
    if request.method == 'POST':
        print(request.form, file=sys.stdout)
        member_id = request.form.get('member_id')
        events = get_events(member_id)
        response = make_response(f"{{'response': {events}}}")
        response.headers = {'Content-Type': 'application/json'}
        return response
    content = render_template('action.html', events=events)
    return content
