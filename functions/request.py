import requests


def request(url, json=False, content=False):
    if json:
        return requests.get(url).json()
    if content:
        return requests.get(url).content
