from flask import Flask, request, render_template, make_response

from volunteer_hours.api.ragic import Ragic

app = Flask(__name__)


class Member:
    """
    A member is a user with an ID that starts with 'LYN'
    """
    def __init__(self):
        self._member_id: str = ''
        self._events: dict[str, int] = {}

    @property
    def member_id(self) -> str:
        """
        Getter for member ID
        :return: stored member ID
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id: str) -> None:
        """
        Setter for member ID
        :param member_id: a valid member ID
        :return: None
        """
        if member_id.startswith('LYN'):
            self._member_id = member_id

    def get_event_names(self) -> list[str]:
        """
        Get a list of events names assigned to the member
        :return: a list of events
        """
        if not self._member_id:
            return []
        events = Ragic().fetch_events(self._member_id)
        for event in events.values():
            self._events[event['Opportunity']] = event['Event ID']
        return list(self._events.keys())

    def get_event_id(self, event_name: str) -> int:
        """
        Find the event ID corresponding to the event name
        :return: an Event ID
        """
        if not self._events or event_name not in self._events:
            raise ValueError('Event not found')
        return self._events[event_name]


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
        member.member_id = member_id
        response = make_response("{{'response': {member_id}}")
        response.headers = {'Content-Type': 'application/json'}
        return response
    events_list = member.get_event_names()
    content = render_template('action.html', events=events_list)
    return content


@app.route('/sent')
def sent_screen() -> str:
    """
    The sent screen to show that the hours have been logged
    :return: content from sent.html with a response from Ragic
    """
    event_name = request.args.get('event')
    event_id = member.get_event_id(event_name)
    Ragic().log_hours(member.member_id, event_id)
    content = render_template('sent.html')
    return content
