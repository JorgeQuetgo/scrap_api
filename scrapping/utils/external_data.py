import requests


def get_hml_data(url):
    result = requests.get(url)
    return result.content
