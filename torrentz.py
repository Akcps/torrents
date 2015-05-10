__author__ = 'ajitkumar'

import requests
from bs4 import BeautifulSoup


class Torrentz:
    def __init__(self):
        pass

    def search(self, search_string):
        payload = {'q':search_string}
        res = requests.get('https://torrentz.com/search', params=payload)
        print res.content


t = Torrentz()
t.search('Game of thrones')



