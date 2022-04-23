import requests


def get():
    return requests.get('http://httpbin.org/status/204').status_code


def post():
    return requests.post('http://httpbin.org/post', data={'x': 1, 'y': 2})
