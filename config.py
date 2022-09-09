#Where configuration will be referenced by the rest of the program (option[configOption] will return true or false)
import string


option = {
    'caseSensitive' : True,
    'Key' : 'Value'
}



#Prints out current config's and gives instructions on next steps within config menu (Two below)
def currentOptions():
    print('\n\nCurrent Configuration Settings: \n')
    for setting in option:
        print(f'{setting} = {option[setting]}')
    print('\nTo edit a configuration setting, enter: \'E\'\nTo leave configuration menu, enter: \'Q\'')


#Exchanges specified options' value to newValue within config menu (One below)
def editOption():
    notFoundOption = True
    #Selects option to be edited
    while notFoundOption:
        user_configOption = input('Enter the name of the config option to edit: ')
        if option.__contains__(user_configOption):
            notFoundOption = False
            newValue = input('Enter new value for option (True / False): ')
            if newValue.lower() == 'true':
                newValue = True
            else:
                newValue = False
            option[user_configOption] = newValue
        else:
            print('Option not found. Please Try Again.')    


#To enter configuration configuration menu
def configMenu():
    editing = True
    while editing:
        currentOptions()
        user_response_currentOptions = input().upper()
        if user_response_currentOptions == 'Q':
            editing = False
        elif user_response_currentOptions == 'E':
            editOption()
        else:
            print()

