import requests


class Connector:
    def __init__(self):
        self.url = "http://161.246.94.167:8000/"

    def postWithData(self, url, data, cookie=None):
        if cookie is not None:
            r = requests.post(self.url+url, data, cookies=cookie)
        else:
             r = requests.post(self.url+url, data)
        print(self.url+url)
        return r, r.cookies

    def post(self, url, cookie=None):
        if cookie is not None:
            r = requests.post(self.url+url,cookies=cookie)
        else:
            r = requests.post(self.url+url)
        return r, r.cookies
