import tools
from datetime import date, datetime # for use of recording the checkout time
from pytz import timezone # for use of recording the checkout time

def sales(c, conn, table, name):
    serial = []
    serialDicIndex = []
    book = dict({})
    today = date.today()
    ddate = today.strftime('%m/%d/%Y') # format the date to MM/DD/YYYY
    tz = timezone("US/Eastern")
    now = datetime.now(tz)
    curTime = now.strftime('%H:%M:%S') # format the time to HH:MM:SS

    while True:
        c.execute('SELECT SERIAL FROM INVENTORY;')
        fetchTup = c.fetchall()
        for i in range(0, len(fetchTup)):
            serialDicIndex.append(fetchTup[i][0])
        dic = dict({}) 
        for i in range(0, len(serialDicIndex)):
            dic.update({serialDicIndex[i] : 0})
        # store all current inventory's serial number into a dictionary, assigning 0 to all inventory

        while True:
            while True:
                getBar = input("Please input serial number from barcode scanner(enter product 7-DIGIT serial number): ").upper()
                if getBar in serialDicIndex:
                    if len(getBar) == 7:
                        serial.append(getBar)
                        c.execute(f'SELECT NAME FROM INVENTORY WHERE SERIAL = \'{getBar}\'')
                        bName = c.fetchall()[0][0]
                        print(f'{bName} has been added to cart')
                        break
                else:
                    print('\nInvalid Input\n')

            if tools.killSwitch('Scanning') == False:
                break
        # ask user to scan barcode until they want to stop

        for i in range(0, len(serial)):
            c.execute('SELECT AMOUNT FROM INVENTORY WHERE SERIAL = "{}";'.format(serial[i])) # get current inventory for specific book
            amount = c.fetchall()[0][0]

            c.execute('UPDATE INVENTORY SET AMOUNT = "{}" WHERE SERIAL = "{}";'.format((amount - 1), serial[i])) # deduct the sold amount from inventory
            conn.commit()

            c.execute('SELECT NAME FROM INVENTORY WHERE SERIAL = "{}";'.format(serial[i]))
            book.update({serial[i] : c.fetchall()[0][0]}) # get book name to match with its serial number
            dic.update({serial[i] : dic.get(serial[i]) + 1}) # increase sold amount of a specific book

        for i in range(0, len(serial)):
            if dic[serial[i]] != 0: # only record sold books into sales history
                c.execute('SELECT ID FROM SALES;')
                idList = c.fetchall()
                c.execute('SELECT * FROM SALES WHERE ID = {};'.format(len(idList)))
                valueInsert = (len(idList) + 1, book.get(serial[i]), 1, ddate, curTime, name, serial[i])
                c.execute('INSERT INTO SALES VALUES {};'.format(valueInsert))
                conn.commit()
                print(f'1 of {valueInsert[1]} has been sold by {name}')
        # commit sales history to database

        if tools.killSwitch('sales')==False:
            break
