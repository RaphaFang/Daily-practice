# create a func to read url
import urllib.request

def read_url(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return html
