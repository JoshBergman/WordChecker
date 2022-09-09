import word_tree_builder

#Create new word path
def newWord(word):
    word_tree_builder.addWord(word)

#Print all nodes
def print_nodes():
    for node in word_tree_builder.nodes:
        node.print_all()


print_nodes()
#There is no visualizer currently so you kinda just gotta chose a few letters and track them down