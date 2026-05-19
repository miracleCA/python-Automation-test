import requests
from config.settings import BASE_URL

class BaseClient:
    def __init__(self, username, password):
        self.auth = (username, password)
        self.base_url = BASE_URL

    def get(self, endpoint, params=None):
        return requests.get(
            f"{self.base_url}{endpoint}",
            auth=self.auth,
            params=params
        )

    def post(self, endpoint, json=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            auth=self.auth,
            json=json
        )

    def put(self, endpoint, json=None):
        return requests.put(
            f"{self.base_url}{endpoint}",
            auth=self.auth,
            json=json
        )

    def patch(self, endpoint, json=None):
        return requests.patch(
            f"{self.base_url}{endpoint}",
            auth=self.auth,
            json=json
        )

    def delete(self, endpoint):
        return requests.delete(
            f"{self.base_url}{endpoint}",
            auth=self.auth
        )