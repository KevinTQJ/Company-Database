import tools

def insert(c, conn, table, position):
    invTuple = ('NAME', 'PRICE', 'AMOUNT', 'CATEGORY', 'AUTHOR', 'PUBLISHER', 'SERIAL')
    empTuple = ('NAME', 'PASSWORD', 'AGE', 'PHONE_NUMBER', 'ADDRESS', 'SALARY', 'HIRE_DATE', 'POSITION_TITLE', 'REPORT_TO')
    salTuple = ('PRODUCT', 'AMOUNT', 'DATE', 'TIME', 'CASHIER', 'SERIAL')
    lis = []

    while True:
        c.execute('SELECT ID FROM {};'.format(table))
        ids = c.fetchall()
        nextId = len(ids) + 1 # as sales history are generated  in chronological order, we use the previous ID to derermine the ID for current sale

        while True:
            try:
                if table == 'inventory':
                    for i in range(0, len(invTuple)):
                        lis.append(input(f'What is the {invTuple[i]} of the new book? '))
                    tupInsert = (nextId, lis[0], float(lis[1]), int(lis[2]), lis[3], lis[4], lis[5], lis[6].upper())
                    
                elif table == 'employee':
                    for i in range(0, len(empTuple)):
                        lis.append(input(f'What is the {empTuple[i]} of the new employee? '))
                    tupInsert = (nextId, lis[0], int(lis[1]), int(lis[2]), int(lis[3]), lis[4], float(lis[5]), lis[6], lis[7], lis[8])

                elif table == 'sales':
                    for i in range(0, len(salTuple)):
                        lis.append(input(f'What is the {salTuple[i]} of the new sales? '))
                    tupInsert = (nextId, lis[0], int(lis[1]), lis[2], lis[3], lis[4], lis[5])

                break
                
            except:
                lis.clear()
                print('\nInput(s) does not match expected data type, try again.\n')

        c.execute('INSERT INTO {} VALUES {};'.format(table, tupInsert))
        conn.commit()

        c.execute('SELECT * FROM {} WHERE ID = {}'.format(table, nextId))
        print(c.fetchall()) # inform user what has been inserted
        print(f'\nThe data listed above has been successfully inserted into the table of {table}\n')
        lis.clear()

        if tools.killSwitch('insert') == False:
            break