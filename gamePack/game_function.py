"""
set the random position of the 3 utensils in level 1 and level 2
"""
import random as rm

from gamePack.game_class import Level 


def random1_position_x1():
    if Level.level_number == 1 and not Level.fix_x1_1:
        x = rm.choice([120,90,90,330,120,0,330,360,390])
    Level.level.fix_x1_1 = 'True'
    return x

def random1_position_y1():
    if Level.level_number == 1 and not Level.fix_y1_1:
        y = rm.choice([30,60,90,120,270,330,330,390,390])
    Level.level.fix_y1_1 = 'True'
    return y
"""
def random1_position_x2():
    return rm.choice([0,0,0,210,180,210,240,360])
def random1_position_y2():
    return rm.choice([150,180,210,210,330,330,330,30])

def random1_position_x3():
    return rm.choice([120,60,90,120,210,240,300,330])
def random1_position_y3():
    return rm.choice([150,390,390,390,120,120,240,240])
""" 


    



    