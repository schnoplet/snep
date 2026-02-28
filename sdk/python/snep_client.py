# sdk/python/snep_client.py
import requests

class SNEPClient:
    def __init__(self, server_url="http://127.0.0.1:5000"):
        self.server_url = server_url.rstrip("/")

    def publish(self, collection, id, data):
        """
        Publish data to the SNEP server
        :param collection: collection name (str)
        :param id: identifier (str)
        :param data: dictionary to store
        :return: response JSON
        """
        url = f"{self.server_url}/{collection}/{id}"
        try:
            r = requests.post(url, json=data)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def fetch(self, collection, id):
        """
        Fetch data from the SNEP server
        :param collection: collection name (str)
        :param id: identifier (str)
        :return: response JSON
        """
        url = f"{self.server_url}/{collection}/{id}"
        try:
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            return {"error": str(e)}