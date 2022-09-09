import word_tree_builder
import config


def checkValidity(inputWord):
        #When caseSensitive(config.py) is False
    if config.option['caseSensitive'] == False:
        word = inputWord.lower()
    else:
        #When caseSensitive(config.py) is not False
        word = inputWord


    root = word_tree_builder.root
    currNode = root
    wasInvalid = False #Used to stop console from printing 'Not Valid' twice when both conditions are met

    for letter in word:
        #When the next letter is not found:
        if currNode.check_letter_validity(letter) == False:
            print("Not Valid")
            wasInvalid = True
            break
        else:
        #When the next letter is found and returns an address:
            currNode = currNode.check_letter_validity(letter)
    #Check for valid if path finished
    if currNode.check_letter_validity('*') == '*':
        print('Valid')
    else:
        #When the path exists but the word is not valid
        if not wasInvalid:
            print('Not Valid')