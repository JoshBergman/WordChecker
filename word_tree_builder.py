import node_definition
import config
import os


#The objects(Letter Nodes) will be kept in the 'nodes' array. {I'm sure there is a better way to do this but this works just fine, I think...}
nodes = []

#Root is important as it is where all search and create algorithms should start. (Default pointer position)
nodes.append(node_definition.Node('Root')) #Initializing root node.
root = nodes[0] #Root pointer


#Function that takes a word and generates it into the tree letter by letter and marks the word as valid
def addWord(word):
    #Helper variables initialized to root
    currNode = root
    prevNode = root

    for letter in word:
        prevNode = currNode
        #Check if letter already exists as a node
        if currNode.letterOptions.__contains__(letter):
            currNode = currNode.letterOptions[letter] #moves pointer to next node
        #Case when the letter is not already an option
        else:
            currNode = node_definition.Node(letter) #Creates new letter node - temporarily stored in currNode
            nodes.append(currNode) #Stores new node in array, so when currNode is updated, the node doesn't get deleted
            prevNode.add_letter_option(letter, currNode) #Adds option for next letter to the last node

    #After word is generated, attach a star to the last letter so that we know the path is valid.
    currNode.add_letter_option('*', '*')
    #Bring the pointers back to root
    currNode = root
    prevNode = root



#To access the word bank file (path provided by user)
def getWordBankPath():
    print('\n\nExample Path: \nC:\Folder1\Folder2\Folder3\wordbank.txt')
    user_path = input("Enter the path of your word bank file: ")
    assert os.path.exists(user_path), "I did not find the file at, "+str(user_path)
    return user_path


#Function to access wordbank from a file, puts all words in list called 'wordBank'
def readFile(path):
    with open (path, 'r') as file:
        fileRead = file.read()
        file.close()
        return fileRead
wordBank = readFile(getWordBankPath()).split()


#Loop to add words to node tree when caseSensitive is False (from config.txt)
if config.option['caseSensitive'] == False:
    for word in wordBank:
        addWord(word.lower())
else:
#Loop to add words to node tree when caseSensitive is not False
    for word in wordBank:
        addWord(word)