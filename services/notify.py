import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'

    def send_event(self, data):
        requests.post(
            url=f'{self.__base_url}/80aec277-ad29-4e11-980f-a6cf36646185',
            json=data,
        )
