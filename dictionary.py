#!/usr/bin/env python3

import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

# def findWord():
#     word = input("Type a word: ")
#     print(data[word])
# findWord()

def translate(word):
    word = word.lower().strip()
    
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn == "yes" or yn == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N" or yn == "n" or yn == "no":
            return "The word doesn't exist. Please double check."
        else:
            return "We didn't understand your entry."
    else:
        get_close_matches(word, data.keys())[0]
        return "Word doesn't exists!"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)