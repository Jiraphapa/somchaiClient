import requests


class Connector:
    def __init__(self):
        self.url = "http://127.0.0.1:8000/"

    def setUrl(self, url):
        self.url = url

    def post(self, url, data):
        res = requests.post(self.url+url, data)
        print(res.text)
