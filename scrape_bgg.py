# Input: keyword, filename
# output: blob of text that is all descriptions
# of games that match that keyword written to the file.

import requests
from xml.etree import ElementTree

url_base = 'https://www.boardgamegeek.com/xmlapi/boardgame/'

def getGamesFromIds(ids):
    query_url = url_base + ''.join(map(str, ids))
    r = requests.get(query_url)
    print r.status_code
    tree = ElementTree.fromstring(r.content)
    return tree

def getDescriptionsFromTree(tree):
    for child in tree:
        print child.tag
        if child.tag == 'boardgame':
            # for k in child:
            #     print k
            print child.find('description').text
