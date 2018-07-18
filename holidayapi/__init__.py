import os
import json
import requests


class Api:
    def __init__(self):
        self.key = os.environ['HOLIDAY_API_KEY']

    def holidays(self, params):
        url = 'https://holidayapi.com/v1/holidays?'

        params['key'] = self.key

        response = requests.get(url, params=params);
        data = json.loads(response.text)

        if ('error' not in data.keys()) and (response.status_code != 200):
            data['error'] = 'Unknown error'

        return data

