"""
A wrapper for the Ragic API
"""
import requests

from volunteer_hours import Config
from volunteer_hours.common.enums import Http, Attendance


class Ragic:
    """
    Use the requests library to talk to the Ragic API
    """
    _base_url = 'https://na3.ragic.com'

    def _get_data(self, api_route: str, params: dict) -> requests.Response:
        """
        Get data from the specified API route.
        """
        url = f'{self._base_url}/{api_route}'
        api_key = Config.ragic_api_key()
        headers = {'Authorization': f'Basic {api_key}'}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == Http.OK:
            print(f"Data sent to {url}.")
        return response

    def _send_data(self, api_route: str, data: dict) -> requests.Response:
        """
        Send data to the specified API route.
        :param api_route: an API route in Ragic
        :param data: data to be sent to Ragic
        :returns: a response from Ragic
        """
        url = f'{self._base_url}/{api_route}'
        api_key = Config.ragic_api_key()
        headers = {'Authorization': f'Basic {api_key}'}
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == Http.OK:
            print(f"Data sent to {url}.")
        return response

    def fetch_events(self, member_id: str) -> dict:
        """
        Get active events that the member signed up for
        :param member_id: the associated member ID
        :returns: events data from Ragic
        """
        conditions = [f'{Attendance.TIMECLOCK_STATUS},eq,Open',
                      f'{Attendance.MEMBERSHIP_ID},eq,{member_id}']
        payload = {'where': conditions, 'api': ''}
        route = Config.ragic_opportunity_route()
        response = self._get_data(route, payload)
        return response.json()
