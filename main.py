import checkWord
import config

#Simple while loop to check words for validity (words are compared against what is provided from the word bank and built into the node tree)
hasntQuit = True
while hasntQuit:
    userInput = input('\nEnter \'Q\' to quit, \'E\' to enter config menu, or a word to check validity: ')
    if userInput.upper() == 'Q':
        hasntQuit = False
    elif userInput.upper() == 'E':
        config.configMenu()
    else:
        checkWord.checkValidity(userInput)
print('Program Successfully Quit')