__author__ = 'ajitkumar'

import requests
from bs4 import BeautifulSoup


class Torrent:

    def __init__(self):
        self.name = ''
        self.link = ''
        self.verified_by = ''
        self.uploaded_date = ''
        self.size = ''
        self.seeds = ''
        self.peers = ''
        self.trackers = []
        self.magnetic_link = {}


def search(search_string):
    try:
        payload = {'q': search_string}
        res = requests.get('https://torrentz.com/search', params=payload)
        soup = BeautifulSoup(res.content)
        links = soup.find_all('dl')
        torrentz_list = []
        for torrent in links[:3]:
            torrentz = Torrent()
            torrent_link = 'https://torrentz.in'
            torrent_link += torrent.a['href']
            torrentz.link = torrent_link
            title_description = torrent.a.contents[-1]
            title_list = torrent.find_all('b')
            title = []
            for title_desc in title_list:
                title.append(title_desc.contents[0])
            title = (' ').join(title)
            title += title_description
            torrentz.name = title
            descriptions = torrent.find_all('span')
            torrentz.verified_by = descriptions[0].contents[0]
            torrentz.uploaded_date = descriptions[1].contents[0]['title']
            torrentz.size = descriptions[3].contents[0]
            torrentz.seeds = descriptions[4].contents[0]
            torrentz.peers = descriptions[5].contents[0]
            torrentz_list.append(torrentz)
        return torrentz_list
    except Exception, excpt:
        print excpt
        return torrentz_list


def search_trackers(torrent_list):
    for torrent in torrent_list:
        try:
            res = requests.get(torrent_list[0].link)
            soup = BeautifulSoup(res.content)
            download_link = soup.find_all('dt')
            download_link_list, magnetic_link = list(), list()
            maglink = dict()
            for link in download_link[:3]:
                if str(link.a['href']).startswith('http'):
                    download_link_list.append(link.a['href'])
                    torrent_site = link.a['href'].split('/')
                    magnet = get_magnetic_link(link.a['href'])
                    if magnet:
                        maglink[torrent_site[2]] = magnet
            torrent.trackers = download_link_list
            torrent.magnetic_link = maglink
        except Exception, excpt:
            print excpt
            torrent.trackers = download_link_list
            torrent.magnetic_link = magnetic_link


def get_magnetic_link(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content)
    magnetic_links = soup.find_all('a')
    maglink = ''
    try:
        for magnetic_link in magnetic_links:
            if str(magnetic_link['href']).startswith('magnet'):
                maglink = magnetic_link['href']
                return maglink
    except Exception, excpt:
        print excpt
        return maglink


def convert_to_json(object_list):
    torrent_list = list()
    for obj in object_list:
        torrent_list.append(obj.__dict__)
    return torrent_list


def search_torrent(params):
    val = search(params)
    search_trackers(val)
    return convert_to_json(val)




