import sys

from flask import Flask, request, render_template

from volunteer_hours.api.ragic import Ragic

app = Flask(__name__)


def get_events() -> list[str]:
    events = Ragic().fetch_events('LYN1701685')
    names = [event['Opportunity'] for event in events.values()]
    return names


@app.route('/')
def main_screen():
    """
    Define the main screen
    """
    content = render_template('index.html')
    return content


@app.route('/action', methods=['POST'])
def action_screen():
    print(request.form, file=sys.stdout)
    member_id = request.form.get('member-id')
    print(member_id)
    events = get_events()
    content = render_template('action.html', events=events)
    return content
