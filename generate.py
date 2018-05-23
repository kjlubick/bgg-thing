import scrape_bgg
import bigram
import nltk

keyword = "boats"
word_frequency_table = {}


def load_text(descriptions, word_table):
    text = ""
    for d in descriptions:
        text += d
	tokens = nltk.word_tokenize(text)
	bigram.updateFrequencyTable(tokens, word_table)
    print "done loading"

ids = scrape_bgg.getIds(keyword)
games_tree = scrape_bgg.getGamesFromIds(ids)
descs = scrape_bgg.getDescriptionsFromTree(games_tree)
load_text(descs, word_frequency_table)
print bigram.createRandom(word_frequency_table)
