import requests

class Connector:
    def __init__(self):
        self.url = "127.0.0.1:8000"

    def setUrl(self, url):
        self.url = url

    def post(self, data):
        #print(requests.post(url=url,data=data).text)
        requests.post(url=self.url,data=data)