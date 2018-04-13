"""
define the random position of the 3 elements in each level of the game
"""
# internal import modules
from random import *
# Local import modules
from gamePack import game_constant as constancy


"""
Item Display Method
"""
def random_position_phial(item):
    """random positioning method for phial"""
    x = 0
    y = 0
    while(item[x][y]!= '_'):
        x = randint(0,14)
        y = randint(0,14)

    item[x][y] = 'p'
    return item

def random_position_needle(item):
    """random positioning method for needle"""
    x = 0
    y = 0
    while(item[x][y]!= '_'):
        x = randint(0,14)
        y = randint(0,14)

    item[x][y] = 'l'
    return item

def random_position_rod(item):
    """random positioning method for rod"""
    x = 0
    y = 0
    while(item[x][y]!= '_'):
        x = randint(0,14)
        y = randint(0,14)

    item[x][y] = 'r'
    return item

"""
Item removal method
"""
def delete_phial(item):
    """method of removing phial"""
    from gamePack.game_class import Level
    x = 0
    y = 0
    while(item[x][y]!= 'p'):
        x = randint(0,14)
        y = randint(0,14)

    item[x][y] = '_'
    Level.backpack += 1 # Add item found
    return item

def delete_needle(item):
    """method of removing needle"""
    from gamePack.game_class import Level
    x = 0
    y = 0
    while(item[x][y]!= 'l'):
        x = randint(0,14)
        y = randint(0,14)

    item[x][y] = '_'
    Level.backpack += 1 # Add item found
    return item

def delete_rod(item):
    """method of removing rod"""
    from gamePack.game_class import Level
    x = 0
    y = 0
    while(item[x][y]!= 'r'):
        x = randint(0,14)
        y = randint(0,14)

    item[x][y] = '_'
    Level.backpack += 1 # Add item found
    return item
