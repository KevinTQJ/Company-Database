import tools

def search(c, table, position):
    while True:
        tools.basicSearch(c, table, position)
        if tools.killSwitch('search') == False:
            break