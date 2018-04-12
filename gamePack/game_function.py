"""
define the random position of the 3 elements in each level of the game
"""
# internal import modules
from random import *



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
