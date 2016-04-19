import requests
def post(data,url):
    #print(requests.post(url=url,data=data).text)
    requests.post(url=url,data=data)