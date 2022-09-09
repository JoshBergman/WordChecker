import node_definition

#Things to test: (^ indicates its been tested)
# ^ __init__ functionality -> thisLetter, letterOptions
# ^ add_letter_option(self, newLetter, nodeAddress)
# ^ check_letter_validity(self, letter_to_be_checked)
# ^ print_all(self)


#Creating two nodes: nodes A -> B (__init__ and add_letter_option)
testNode1 = node_definition.Node('A')
testNode2 = node_definition.Node('B')

testNode1.add_letter_option('B', testNode2)
# testNode1.print_all()
# testNode2.print_all()


#Adding star at end of B to mark path as valid, then checking for validity
testNode2.add_letter_option('*', '*')
print('\nShould return a \'*\':')
print( testNode2.check_letter_validity('*') )


#Checking for a possible letter in the path
print(f'\nShould return False: ')
print( testNode2.check_letter_validity('R') )

print(f'\nShould return address for testNode2 (which is: {testNode2})')
print( testNode1.check_letter_validity('B') )