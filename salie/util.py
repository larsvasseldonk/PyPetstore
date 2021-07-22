'''
This modules contains functions to print the menu.

'''

def print_main_menu():
    '''This function prints the main menu of the program.'''
    print('\n-- Main Menu --\n')
    print('1. Orders')
    print('2. Customers')
    print('3. Products')
    print('4. Sales')
    print('0. Exit\n')
    return input('Enter your choice [1-4]: ')
