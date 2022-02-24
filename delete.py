import tools

def delete(c, conn, table, position):
    while True:
        tools.basicSearch(c,table, position)
        try:
            if table == 'inventory':
                ask = input('\nWhat is the ID of the book you want to delete?')
            
            elif table == 'employee':
                ask = input('\nWhat is the ID of the employee you want to delete?')

            elif table == 'sales':
                ask = input('\nWhat is the ID of the sales history you want to delete?')

            c.execute('DELETE FROM {} WHERE ID = "{}";'.format(table, ask))
            conn.commit()
            
            print(f'ID = {ask} has been deleted from {table}')

            if tools.killSwitch('delete') == False:
                break

        except:
            print('\nInvalid Input.\n')
        
