# Input: keyword, filename
# output: blob of text that is all descriptions
# of games that match that keyword written to the file.

import requests
from xml.etree import ElementTree


def getIds(keyword):
    url = 'https://www.boardgamegeek.com/xmlapi2/search?type=boardgame&query='+keyword
    # if keyword == 'hot':
    #     url = 'https://www.boardgamegeek.com/xmlapi2/hot?type=boardgame'
    r = requests.get(url)
    if r.status_code >= 400:
        return 'ERROR'
    tree = ElementTree.fromstring(r.content)
    ids = []
    for child in tree:
        ids += [child.attrib['id']]
    return ids

print getIds('boat')


# url = 'https://www.boardgamegeek.com/xmlapi/boardgame/2536,1234,857'

# r = requests.get(url)

# tree = ElementTree.fromstring(r.content)

# for child in tree:
#     print child.tag
#     if child.tag == 'boardgame':
#         print child.find('description').text