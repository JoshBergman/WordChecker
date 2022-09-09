#Definition of the Node used by each letter to determine validity of words
class Node:
    def __init__(self, thisLetter):
        self.thisLetter = thisLetter #This is the letter that the node represents
        self.letterOptions = {} #This is all possible next letters. If a star ('*':'*') is included in this dictionary, the 'word path' is considered valid.

#Adds a new letter to possible paths, meaning there is a node representing each letter added here. If a star is added, the word path is considered valid.
    def add_letter_option(self, newLetter, nodeAddress):
        self.letterOptions[newLetter] = nodeAddress

#Returns a node address if it is valid, returns a star when checked for a star, if not valid returns False
    def check_letter_validity(self, letter_to_be_checked):
        if self.letterOptions.__contains__(letter_to_be_checked):
            return self.letterOptions[letter_to_be_checked]
        else:
            return False

#Print Information for testing
    def print_all(self):
        print(f'\n\nSelf: {self},\nthisLetter: {self.thisLetter},\nletterOptions: {self.letterOptions}\n')