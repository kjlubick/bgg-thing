# Input: keyword, filename
# output: blob of text that is all descriptions
# of games that match that keyword written to the file.

import requests
from xml.etree import ElementTree

url = 'https://www.boardgamegeek.com/xmlapi/boardgame/2536,1234,857'

r = requests.get(url)

print r.status_code

tree = ElementTree.fromstring(r.content)

print tree
#root = tree.getroot()
for child in tree:
    print child.tag
    if child.tag == 'boardgame':
        # for k in child:
        #     print k
        print child.find('description').text