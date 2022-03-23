from flask import Flask, request, render_template, make_response

from volunteer_hours.api.ragic import Ragic

app = Flask(__name__)


class Member:
    """
    A member is a user with an ID that starts with 'LYN'
    """
    def __init__(self):
        self._member_id = ''

    def set_member_id(self, member_id: str) -> None:
        """
        Setter for member ID
        :param member_id: a valid member ID
        :return: None
        """
        if member_id.startswith('LYN'):
            self._member_id = member_id

    def get_events(self) -> list[str]:
        """
        Get a list of events assigned to the member
        :return: a list of events
        """
        if not self._member_id:
            return []
        events = Ragic().fetch_events(self._member_id)
        names = [event['Opportunity'] for event in events.values()]
        return names


member = Member()


@app.route('/')
def main_screen() -> str:
    """
    The main page for scanning QR code
    :return: content from index.html
    """
    content = render_template('index.html')
    return content


@app.route('/action', methods=['GET', 'POST'])
def action_screen() -> str:
    """
    The action page for selecting an event to sign in/out for
    :return: content from action.html with events from Ragic
    """
    if request.method == 'POST':
        member_id = request.form.get('member_id')
        member.set_member_id(member_id)
        response = make_response("{{'response': {member_id}}")
        response.headers = {'Content-Type': 'application/json'}
        return response
    events_list = member.get_events()
    content = render_template('action.html', events=events_list)
    return content
