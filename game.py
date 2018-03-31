#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MacGyver labyrinth game

Python script with graphic management by 'pygame' containing the following
modules:
'game_class' and 'game_constant'
Images (labyrinth / personas / objects)
file (s) 'TXT' for labyrinth strategy
"""

# externel modules
import pygame as pg
from pygame.locals import *

# local libraries
from gamePack import game_constant as gc

""" window management
    Adaptation of the window according to the size of sprites
"""
pg.init()

# Initiation of window
window = pg.display.set_mode((gc.window_size, gc.window_size))

# icon of the window
icon = pg.image.load(gc.window_icon)
pg.display.set_icon(icon)
# Title of the window
pg.display.set_caption(gc.window_title)
