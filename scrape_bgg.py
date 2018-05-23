# Input: keyword, filename
# output: blob of text that is all descriptions
# of games that match that keyword written to the file.

import requests
from xml.etree import ElementTree

url_base = 'https://www.boardgamegeek.com/xmlapi/boardgame/'

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

def getGamesFromIds(ids):
    query_url = url_base + ','.join(ids)
    r = requests.get(query_url)
    print r.status_code
    tree = ElementTree.fromstring(r.content)
    return tree

def getDescriptionsFromTree(tree):
    desc = []
    for child in tree:
        if child.tag == 'boardgame':
            desc.append(child.find('description').text)
    return desc
