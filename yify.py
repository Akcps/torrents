__author__ = 'ajitkumar'
import ConfigParser
import io
import requests
import os
import pdb
dir = os.path.dirname(os.path.abspath(__file__))

with open("external-url.yaml") as f:
    external_url_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(external_url_config))


class Yify:
    def __init__(self):
        pass

    def get_movies_list(self):
        yify_url = config.get('yify','movies-list')
        res = requests.get(yify_url)
        data = res.json()
        print data
        movies = data['data']['movies']
        movies_name = list()
        for movie in movies:
            movies_name.append(movie['title'])
        print movies_name
        return movies_name




y = Yify()
y.get_movies_list()





