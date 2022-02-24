import search, sales, insert, update, delete
import colorama

def killSwitch(fname):
    while True:
        check = input('\nDo you wish to repeat the operation: \'' + fname + '\' again?(Y/N)').lower()
        if check == 'y':
            return True
        elif check == 'n':
            return False
        else:
            print('Invalid Input.')
    


def printNice(c, table, t, position):
    c.execute('SELECT * FROM {};'.format(table))
    tableInfo = tuple([tuple[0] for tuple in c.description]) # get headers of sepcific table

    if position == 'Manager' and table == 'employee':
        for i in tableInfo:
            print(f"{i:<20}", end='')
        for i in range(0, len(t)):
            print()
            for j in range(0, len(t[i])):
                if j == 2: #Password
                    print("[Access Denied]     ", end = '')
                else:
                    print(f"{t[i][j]:<20}", end = '')
    # avoid showing password to anyone except the owner

    else:
        for i in tableInfo:
            print(f"{i:<20}", end = '')
        for i in range(0, len(t)):
            print()
            for j in range(0, len(t[i])):
                print(f"{t[i][j]:<20}", end = '')
    # print out selected table


def basicSearch(c, table, position):
    while True:
        keyType, keyword = askKey(c, table)
        c.execute('SELECT * FROM {} WHERE {} LIKE "%{}%"; '.format(table, keyType, keyword))
        t = c.fetchall()
        if not t:
            print('\nKeyword not found\n')
            continue
        elif t:
            break
    printNice(c, table, t, position)  
# look up all info that the user requested


def askKey(c, table):
    invTuple = ('ID', 'NAME', 'PRICE', 'AMOUNT', 'CATEGORY', 'AUTHOR', 'PUBLISHER', 'SERIAL')
    empTuple = ('ID', 'NAME', 'PASSWORD', 'AGE', 'PHONE_NUMBER', 'ADDRESS', 'SALARY', 'HIRE_DATE', 'POSITION_TITLE', 'REPORT_TO')
    salTuple = ('ID', 'PRODUCT', 'AMOUNT', 'DATE', 'TIME', 'CASHIER', 'SERIAL')
    keyInt = ('ID', 'AMOUNT', 'AGE', 'PHONE_NUMBER')
    keyFloat = ('PRICE', 'SALARY')
    keyString = ('NAME', 'CATEGORY', 'AUTHOR', 'PUBLISHER', 'SERIAL', 'PRODUCT', 'DATE', 'TIME', 'CASHIER', 'ADDRESS', 'SALARY', 'HIRE_DATE', 'POSITION_TITLE', 'REPORT_TO')

    while True:
        keyType = input('''Which kind of keyword would you like to use?(Please enter the exact keyword)
For Inventory:
    ID, NAME, PRICE, AMOUNT, CATEGORY, AUTHOR, PUBLISHER, SERIAL
For Sales History:
    ID, PRODUCT, AMOUNT, DATE, TIME, CASHIER
For Employee:
    ID, NAME, AGE, PHONE_NUMBER, ADDRESS, SALARY, HIRE_DATE, POSITION_TITLE, REPORT_TO
''').upper()

        try:
            if (table == 'employee' and keyType in empTuple) or (table == 'inventory' and keyType in invTuple) or (table == 'sales' and keyType in salTuple): # identify whether the keyword type is included in the corresponding table
                if keyType in keyInt:
                    keyword = int(input('What is the keyword?'))
                    break
                elif keyType in keyFloat:
                    keyword = str(input('What is the keyword?'))
                    break
                elif keyType in keyString:
                    keyword = input('What is the keyword?')
                    break
                else:
                    print('\nKeyword not found, please try again\n')
            else:
                    print('\nKeyword Type not in selected table, please try again\n')
        except:
            print('\nInput data type does not match database\n')

    return keyType, keyword
# ask the user to input keyword type and keyword for other methods

def idCantBeChanged():
    keyTypeExact = input('Please enter the exact information type want to be updated: ')
    if (keyTypeExact) == "ID":
        print("\nYou can't change the ID")
        return keyTypeExact, True
    else:
        return keyTypeExact, False


def meunOutput(c, conn, name, position, op1, op2):
    if op1 == 1:
        dataType = 'inventory'
    elif op1 == 2:
        dataType = 'sales'
    elif op1 == 3:
        dataType = 'employee'

    if op2 == 1:
        print(colorama.Fore.LIGHTMAGENTA_EX)
        sales.sales(c, conn, dataType, name)
    elif op2 == 2:
        print(colorama.Fore.YELLOW)
        search.search(c, dataType, position)
    elif op2 == 3:
        print(colorama.Fore.CYAN)
        update.update(c, conn, dataType, position)
    elif op2 == 4:
        print(colorama.Fore.LIGHTCYAN_EX)
        insert.insert(c, conn, dataType, position)
    elif op2 == 5:
        print(colorama.Fore.LIGHTYELLOW_EX)
        delete.delete(c, conn, dataType, position)
    elif op2 == 6:
        return True
# call correspoing functional methods
# since including this part in the menu method will result in the warning "cyclomatic complexity too high"
# to solve this, we seperated the menu() into three parts: menuOutput(), menu1() and menu2(), which you can see menu1() and menu2() in main()