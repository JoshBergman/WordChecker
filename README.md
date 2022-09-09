# WordChecker
Created By: Joshua Bergman

Desciption:

Program that checks if a word is included in a word list provided by the user.
This program is not fully complete, but fully functional.




How To Use:

1) Prepare word bank, add it to a text file, then copy the path to that .txt file for later.
2) Run main.py in .../WordChecker directory, the program should guide you from here.

To prepare a word bank) 1) Put words in a text file(.txt) and seperate each word with whitespace (a space or new line)
2) TIP: to add a phrase, seperate the words with dashes so it is counted as one large word.




How It Works:

TLDR: This program generates a node tree based on the word bank provided.

1) Generating the node tree (Main part)
The word bank is put into a list of individual word, which are each added to the node tree letter by letter.
Each letter is a node in the tree, but no letter is duplicate, making this very efficient for search of large word banks.
Each letter node(node) is added in the order provided, off of the root node(starting point), then after each subsequent letter.
If the next letter already exists off of the current node, the letter is not added, instead you simply move to the current letter node.
At the end of each word a marker is place on the current node to indicate that the node path is considered valid.

(This explaination is probably horrible, so here is a picture I hope it helps)
This example would be for the word bank: (Apple, Dog, Dig, Digger, Example)(* Represents marker indicating the path is valid)
            Root node -> (Root)
                        /   |  \
                     (A)   (D) (E)
                    /      / \   \
                 (p)    (i)  (o)  (x)
                 /      /      |    \
                (p)    (g)    (g)   (a)
                 |      | \     \     \
                (l)    (g) (*)  (*)   (m)
                 |      |              |
                (e)    (e)            (p)
                 |      |              |
                (*)    (r)            (l)
                        |              |
                       (*)            (e)
                                       |
                                      (*)


2) Comparing words against the word tree.
The user is able to input words, which are then compared to the node tree letter by letter and if it finds a path that has a marker, the word is returned as valid. Any failure to find a next node considers the user input as invalid. Any failure to find a marker even when the path was able to be fully followed results in the input being invalid.




Known Issues:

-Config options reset each time you run the program (if you changed them in the program)
(This is due to having them only hard-coded for the time being. You could manually adjust them in config.py and they will stay.)




Features To Be Added:

-Visual interface
-Less user input (Better pathing and more of a plug-and-play approach)
-Ability to save node tree for large word banks that are inefficient to re-render every time