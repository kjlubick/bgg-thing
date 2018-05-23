import json
import random

def getText(tweet):
    return tweet["text"]

def addWordPairToFrequencyTable(current_word, next_word, frequency_table):
    if current_word not in frequency_table:
        frequency_table[current_word] = []
    frequency_table[current_word].append(next_word)

def updateFrequencyTable(words, frequency_table):
    for i in range(len(words)):
        # Check to make sure we're not on the last word
        # since the last word won't have a valid next word.
        if i + 1 < len(words):
            current_word = words[i]
            next_word = words[i+1]
            addWordPairToFrequencyTable(current_word, next_word, frequency_table)

def createRandom(word_frequency_table):
    output = ""
    current_word = random.choice(word_frequency_table.keys())
    words = 0
    while words < 30:
        output += current_word + " "
        if current_word not in word_frequency_table.keys():
            break
        possible_next_words = word_frequency_table[current_word]
        current_word = random.choice(possible_next_words)
        words += 1
    return output
