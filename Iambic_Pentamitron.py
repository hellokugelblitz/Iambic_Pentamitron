"""
                  ___           ___           ___                       ___                    ___           ___           ___           ___           ___           ___                       ___           ___           ___           ___     
      ___        /\  \         /\__\         /\  \          ___        /\  \                  /\  \         /\  \         /\__\         /\  \         /\  \         /\__\          ___        /\  \         /\  \         /\  \         /\__\    
     /\  \      /::\  \       /::|  |       /::\  \        /\  \      /::\  \                /::\  \       /::\  \       /::|  |        \:\  \       /::\  \       /::|  |        /\  \       \:\  \       /::\  \       /::\  \       /::|  |   
     \:\  \    /:/\:\  \     /:|:|  |      /:/\:\  \       \:\  \    /:/\:\  \              /:/\:\  \     /:/\:\  \     /:|:|  |         \:\  \     /:/\:\  \     /:|:|  |        \:\  \       \:\  \     /:/\:\  \     /:/\:\  \     /:|:|  |   
     /::\__\  /::\~\:\  \   /:/|:|__|__   /::\~\:\__\      /::\__\  /:/  \:\  \            /::\~\:\  \   /::\~\:\  \   /:/|:|  |__       /::\  \   /::\~\:\  \   /:/|:|__|__      /::\__\      /::\  \   /::\~\:\  \   /:/  \:\  \   /:/|:|  |__ 
  __/:/\/__/ /:/\:\ \:\__\ /:/ |::::\__\ /:/\:\ \:|__|  __/:/\/__/ /:/__/ \:\__\          /:/\:\ \:\__\ /:/\:\ \:\__\ /:/ |:| /\__\     /:/\:\__\ /:/\:\ \:\__\ /:/ |::::\__\  __/:/\/__/     /:/\:\__\ /:/\:\ \:\__\ /:/__/ \:\__\ /:/ |:| /\__\
 /\/:/  /    \/__\:\/:/  / \/__/~~/:/  / \:\~\:\/:/  / /\/:/  /    \:\  \  \/__/          \/__\:\/:/  / \:\~\:\ \/__/ \/__|:|/:/  /    /:/  \/__/ \/__\:\/:/  / \/__/~~/:/  / /\/:/  /       /:/  \/__/ \/_|::\/:/  / \:\  \ /:/  / \/__|:|/:/  /
 \::/__/          \::/  /        /:/  /   \:\ \::/  /  \::/__/      \:\  \                     \::/  /   \:\ \:\__\       |:/:/  /    /:/  /           \::/  /        /:/  /  \::/__/       /:/  /         |:|::/  /   \:\  /:/  /      |:/:/  / 
  \:\__\          /:/  /        /:/  /     \:\/:/  /    \:\__\       \:\  \                     \/__/     \:\ \/__/       |::/  /     \/__/            /:/  /        /:/  /    \:\__\       \/__/          |:|\/__/     \:\/:/  /       |::/  /  
   \/__/         /:/  /        /:/  /       \::/__/      \/__/        \:\__\                               \:\__\         /:/  /                      /:/  /        /:/  /      \/__/                      |:|  |        \::/  /        /:/  /   
                 \/__/         \/__/         ~~                        \/__/                                \/__/         \/__/                       \/__/         \/__/                                   \|__|         \/__/         \/__/    
"""

import random

#A word or 
VOWELS = "aeoiu"

class Word:
    def __init__(self, text, syllables):
        self.text = text
        self.syllables = syllables

#This is to count sylables duh.
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def get_words(filename):
    file = open(filename, 'r')
    words = []

    for line in file:
        words.append(line)

    file.close()

    return words

def isolate_sylables():
    pass

def parse_adjectives():
    pass

def craft_poem(feet):
    adjectives_text = get_words("Adjectives.txt")
    adjectives = []

    nouns_text = get_words("Nouns.txt")
    nouns = []
    for word in range(len(nouns_text)):
        nouns.append(Word(nouns_text[word],syllable_count(nouns_text[word])))

    
    for word in range(len(adjectives_text)):
        adjectives.append(Word(adjectives_text[word],syllable_count(adjectives_text[word])))
    
    """
    for i in range(len(adjectives)):
        print(adjectives[i].text, adjectives[i].syllables)

    for i in range(len(nouns)):
        print(nouns[i].text, nouns[i].syllables)
    """

    syllable_max = feet*2

    #grab random adjective, subtract it from total, random noun subtract it from total and so on, if too much look for a smaller word
    poem = " "
    while syllable_count(poem) < syllable_max:
        noun = nouns[random.randint(0,len(nouns))]
        if syllable_count(poem) + syllable_count(noun.text) <= syllable_max:
            poem += noun.text
            poem += str(noun.syllables)
        else:
            continue

        adjective = adjectives[random.randint(0,len(adjectives))]
        if syllable_count(poem) + syllable_count(adjective.text) <= syllable_max:
            poem += adjective.text
            poem += str(adjective.syllables)
        else:
            continue

    return poem

#Used to fetch a word of a certain sylable count
def fetch_word():
    pass



def main():

    print(craft_poem(5))

main()