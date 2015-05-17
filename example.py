__author__ = 'ajitkumar'

from torrentz import search_torrent
search_results = search_torrent('Game of Thrones')
# print the search results
print search_results


for result in search_results:
    print result
