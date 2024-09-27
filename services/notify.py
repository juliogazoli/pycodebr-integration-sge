import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'

    def send_event(self, data):
        requests.post(
            url=f'{self.__base_url}/af8e8b41-bfde-42af-9efa-269fa16724bf',
            json=data,
        )
