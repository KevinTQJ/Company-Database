import tools

def update(c, conn, table, position):
    check = True

    while True:
        tools.basicSearch(c, table, position)
        id = int(input('\nPlease enter the item\'s ID want to be updated:'))

        while check:
            keyTypeExact, check = tools.idCantBeChanged()
        keywordNew = input('\nPlease enter the updated information: ')

        c.execute('UPDATE {} SET {} = "{}" WHERE ID = "{}";'.format(table, keyTypeExact, keywordNew, id))
        conn.commit()
        
        print(f'ID = {id}\'s {keyTypeExact} has been updated to {keywordNew}')
        if tools.killSwitch('update') == False:
            break

