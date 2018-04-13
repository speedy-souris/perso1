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
def random_position(item,character):
    """random positioning method for item"""
    x = 0
    y = 0
    while(item[x][y]!= '_'):
        x = randint(0,14)
        y = randint(0,14)

    item[x][y] = character
    return item

"""
Item removal method
"""
def delete(item,character):
    """method of removing item"""
    from gamePack.game_class import Level
    x = 0
    y = 0
    while(item[x][y]!= character):
        x = randint(0,14)
        y = randint(0,14)

    item[x][y] = '_'
    Level.backpack += 1 # Add item found
    return item
