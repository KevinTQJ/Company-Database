# Assignment Name: Company Database
# 
# TODO: Create a data base and corresponding management system for Francine's Book Store
# 
# Date and Time completed: 2021-03-24 17:58
#
# Team member: Kevin Wu, Kevin Zhao, Neil Zhou

import sqlite3 # for use of sqlite databse
import colorama # for change of text colour
from stdiomask import getpass # for hiding the password to prevent snooping 
import tools

colorama.init()# initialize text colour

def security(c):
    print(colorama.Fore.LIGHTCYAN_EX)
    check = check1 = check2 = True
    c.execute('SELECT ID FROM EMPLOYEE;')
    ids = c.fetchall()
    idAmount = len(ids)
    while check:
        while check1:
            try:
                ID = input('''Welcome to Francine’s Book Store Management System, Please login!
ID: ''')
                int(ID) is type(int)# terminate the loop when input is not a integer(because add int() at ln 23 will result in an unknown bug)
                if int(ID) > idAmount or int(ID) <= 0:
                    raise Exception
                check1 = False
            except:
                print('\nInvalid input, try again\n')

        while check2:
            try:
                password = int(getpass("Password: "))
                check2 = False
            except:
                print('\nInvalid input, try again\n')
        
        c.execute(f'SELECT PASSWORD, NAME, POSITION_TITLE FROM EMPLOYEE WHERE ID = {ID};')
        p = c.fetchall()
        if p[0][0] == password:
            print('Login Successfully')
            check = False
        else:
            print('\nPassword does not match ID, please try again\n')
            check1 = check2 = True
        
    name = p[0][1] 
    position = p[0][2]
    return name, position



def menu1(c, conn, name, position):
    print(colorama.Fore.GREEN)
    if position == 'Cashier':
        access = 'checkout item, look up sales history and inventory'
    elif position == 'Manager':
        access = 'do anything, except deleting any data and manipulate employee information'
    elif position == 'Owner':
        access = 'do anything'

    check1 =  True
    while check1:
        while True:
            try:
                op1 = int(input(f'''Hi, {name}, Your position is: {position}
Your are able to: {access}
Select information type:
1 - Inventory 
2 - Sales History (For customer checkout, please select this one)
3 - Employee
4 - LogOut
'''))
                break
            except:
                print('\nPlease enter a corresponding NUMBER\n')

        if op1 == 3 and position == 'Cashier':
            print('\nAccess denied: Higher level authentication required, Try again\n')
        elif op1 < 1 or op1 > 4:
            print('\nInvalid input, try again\n')
        elif op1 == 4:
            return 4
        else:
            return op1
            check1 = False



def menu2(c, conn, name, position, op1):
    check2 = True
    while check2:
        while True:
            try:
                op2 = int(input('''\nSelect an operation:
1 - Sales
2 - Search
3 - Update
4 - Insert
5 - Delete
6 - Return to previous menu
'''))
                break
            except:
                print('\nPlease enter a corresponding NUMBER\n')

        if op2 < 1 or op2 > 6:
            print('\nInvalid input, try again\n')
        elif position == 'Cashier':
            if op2 == 3  or op2 == 4 or op2 == 5:
                print('\nAccess denied: Higher level authentication required\n')
            else:
                return op2
                check2 = False
        elif position == 'Manager':
            if op2 == 5 or (op1 == 3 and op2 == 3) or (op1 == 3 and op2 == 4):
                print('\nAccess denied: Higher level authentication required\n')
            else: 
                return op2
                check2 = False
        else:
            return op2
            check2 = False



def main():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    while True:
        name, position = security(c)
        while True:
            op1 = menu1(c, conn, name, position)
            if op1 == 4:
                break
            op2 = menu2(c, conn, name, position, op1)
            if tools.meunOutput(c, conn, name, position, op1, op2):
                continue
            if tools.killSwitch('menu') == False:
                break

        while True:
          prompt = input('You have successfully logged off, EXIT the System? (or return to login page) (Y/N)').lower()
          if(prompt == 'y' or prompt == 'n'):
              break
          else:
              print("\nInvalid Input.\n")
        if (prompt == 'y'):
            break

    c.close()
    conn.close()

main()
