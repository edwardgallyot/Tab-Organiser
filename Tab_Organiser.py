#! usr/bin/env bash

import webbrowser
import sys
import pyperclip
import shelve
import pyinputplus as pyip
import re

Tab_Categorys = shelve.open('TabCategorys')


# A function to save from the clipboard into the database

def save(category):
    y = pyperclip.paste()
    if category in list(Tab_Categorys.keys()):
        Tab_Categorys[category] = Tab_Categorys[category] + [y, ]
    else:
        Tab_Categorys[category] = [y, ]


# A function to delete a category in the database

def deletetabs(category):
    if category in Tab_Categorys.keys():
        del Tab_Categorys[category]
        print(f'You removed {category} from TabCategorys.db ')
    else:
        print("That's not a category boss man!")


# A function to list everything in the database

def listalltabs():
    for key in Tab_Categorys.keys():
        n = 1
        print(f'Tabs in {key} = ')
        for y in Tab_Categorys[key]:
            print(str(n) + '. ' + y)
            n = n + 1


# A function to list a specific key in the database

def listtab(category):
    if category in Tab_Categorys.keys():
        n = 1
        for y in Tab_Categorys[category]:
            print(f'{n}. {y}')
            n = n + 1
    else:
        print("That's not a real choice!")


# A function to print everything inside a category
# This helps the user to choose what to remove/open if they want to remove or open it respectively
def printinsidecategorys(category):
    n = 1
    for y in (Tab_Categorys[category]):
        print(str(n) + '. ' + y)
        n = n + 1


# A function to remove a tab (y) from a category (x)
def removetab(category, url):
    z = Tab_Categorys[category]
    del z[url]
    Tab_Categorys[category] = z


# A function to check whether x is in a category and open it if it is
def openalltabs(category):
    if category in Tab_Categorys.keys():
        for y in Tab_Categorys[category]:
            webbrowser.open(y)
    else:
        print(f'No URLs found for the keyword {category}')


# A function to open a tab (x) in a category (y)
def opentab(category, url):
    webbrowser.open(Tab_Categorys[category][url])


# Main program loop
while True:
    # User input for their choice.
    while True:
        a = pyip.inputStr('''Use this program to save a URL from Chrome, from the clipboard to a category in a database. 
    
You can choose to 'save' your tab in the clipboard to the database under a category.
You can choose to 'delete' your category from the database.
You can choose to 'remove' a specific tab in your chosen category.
You can choose to 'open' a specific tab in your chosen category.
You can choose to 'openall' the tabs in a category in your default browser.
You can choose to 'listall' categorys from the database and the tabs within them.
You can choose to 'list' a particularly category and the tabs within it.

Please type 'save', 'delete', 'remove', 'open', 'openall', 'listall' or 'list' below:
''')

        aregex = re.compile(r'save|delete|openall|open|listall|list|remove')
        mo = aregex.search(a)
        if mo is None:
            print('Try again!\n')
        else:
            break
    # User input if save is chosen
    if a == 'save':
        b = pyip.inputStr(f'''Which category would you like to save your category under your choices are:
        
{list(Tab_Categorys.keys())} 
    
You can also choose a new name for your category if you would like!
Please type your category name below:
''')
        save(b)
        print(f"You saved {str(pyperclip.paste())} to {b}")
    # User input if delete is chosen
    elif a == 'delete':
        while True:

            b = pyip.inputStr(f'''Which category would you like to delete? Your choices are:
            
{list(Tab_Categorys.keys())} 
            
Please type your category name below:
''')
            while True:
                c = pyip.inputYesNo("Are you sure you want to delete this category?\n")
                if c == 'yes':
                    deletetabs(b)
                    break
                if c == 'no':
                    print("Fair play fella...")
                    break
            break
    # User input if open is chosen
    elif a == 'openall':
        while True:
            b = pyip.inputStr(f'''Which category would you like to open? Your choices are:
            
{list(Tab_Categorys.keys())} 
            
Please type your category name below:
''')
            openalltabs(b)
            break
    # User input if listall is chosen
    elif a == 'listall':
        listalltabs()
    # User input if list is chosen
    elif a == 'list':
        while True:
            b = pyip.inputStr(f'''Which category would you like to get the list of tabs from? Your choices are:

{list(Tab_Categorys.keys())} 

Please type your category name below:
''')
            listtab(b)
            break
    # User input if remove is chosen
    elif a == 'remove':
        while True:
            a = pyip.inputStr(f'''Which category would you like to remove from? Your choices are:

{list(Tab_Categorys.keys())} 

Please type your category name below:
''')
            if a not in list(Tab_Categorys.keys()):
                print('That is not a real category!')
                break
            printinsidecategorys(a)
            b = pyip.inputInt(f'Please type the number of the address would you like to delete from {a}?\n')
            yesno = pyip.inputYesNo('Are you sure you want to delete this?\n')
            if yesno is 'yes':
                print('')
            elif yesno is 'no':
                print("That's all good chief!")
                break
            if b < 1 or b > (len(list(Tab_Categorys[a]))):
                print('That aint right! Try again...')
                break
            else:
                print(f'You removed {Tab_Categorys[a][(b - 1)]} from {a}')
                b = b - 1
                removetab(a, b)
                break
    # User input if open is chosen
    elif a == 'open':
        while True:
            a = pyip.inputStr(f'''Which category would you like to open from? Your choices are:

{list(Tab_Categorys.keys())} 

Please type your category name below:
''')
            if a not in list(Tab_Categorys.keys()):
                print('That is not a real category!')
                break
            printinsidecategorys(a)
            b = pyip.inputInt(f'Please type the number of the address would you like to open from {a}?\n')
            if b < 1 or b > (len(list(Tab_Categorys[a]))):
                print('That aint right! Try again...')
                break
            else:
                b = b - 1
                opentab(a, b)
                print(f'You opened {Tab_Categorys[a][b]} from {a}')
                break
    else:
        print('You appear to have entered multiple inputs...')
    x = pyip.inputYesNo('Do you want to continue? Please answer Yes/No \n')
    # Continue?
    if x == 'yes':
        continue
    if x == 'no':
        print('Thank you for using my Tab Organizer!')
        sys.exit()

Tab_Categorys.close()
