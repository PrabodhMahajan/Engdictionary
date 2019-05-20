# The Best way to load the JSON data is to use Python Dictionaries:
#In Dictionary it'd be too easy to access the value from a key.

#Import JSON module
import json

#Import from difflib lib - > get_close_matches module (We're making our program suggest other similar word/s accurately)
from difflib import get_close_matches

#Loading the data into dictionary in Python
data = json.load(open("dictionary.json"))

#In order to make a program work we'll not use multiple iterations and such scenarios, rather we'll create a function that gets the key (word) and find the value(definition/s) of the specific word.
#Defining the function
def meaning(word):
    
#Making the letters entered by user case insensitive
    word = word.lower()
    
    if word in data:
        return data[word]
    elif word.title() in data:   # For Noun e.g: london - > London
        return data[word.title()]
    elif word.upper() in data:   # For Acronyms like USA or NASA
        return data[word.upper()]
    
#The Program will auto-suggest the similar words associated and you entered and You'll answer it as Yes or No, and also will confirm similarity check of the user entered word.
    elif len(get_close_matches(word,data.keys()))>0:
        UserInput = input("Did you mean %s instead?\n Enter Y for Yes or N for No::"%get_close_matches(word,data.keys())[0])
        if UserInput == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif UserInput == "N":
            return "\n We're updating our app by adding more words, You'll be notified when the update is available"
        else:
            return "\n I didn't get that, Can you please recheck it."
        
    
#If the word is not in the dictionary.
    else:                                         
        return "The Word is not in the dictionary since we're updating it. Inconvenience regretted."    

word = input("Enter the word you want to find the meaning of:\n")

#To show the output in the Command Line you need to print out the function and the parameter/s
output = (meaning(word))   #Optimizing the program to show meanings on new lines, when a word has more than one meaning.
if type(output) == list:
    for separateMeaning in output:
        print(separateMeaning)
else:
    print(output)

''' Comparing the similarity ratio between two words: Might be useful when the user enters Rainn or raain instead of Rain.
import difflib
from difflib import SequenceMatcher
SequenceMatcher(None,"rainn","rain").ratio() for Similarity Ratio.
'''



