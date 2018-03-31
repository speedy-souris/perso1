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

"""
Main loop of the game
"""
maintain = 1
while maintain:
    # home menu display
    menu = pg.image.load(gc.menu_picture).convert()
    window.blit(menu,(0,0))

    # Refresh the window
    pg.display.flip()

    # Reset to one the variables
    maintain_game = 1
    maintain_home = 1

    """
    home loop of the game
    """
    while maintain_home:
        for event in pg.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                maintain_home = 0
                maintain_game = 0
                maintain = 0
                # Variable of choice ==> start of the game
                choice = 0
            elif event.type == KEYDOWN:
                # launch level 1
                if event.key == K_F1:
                    maintain_home = 0
                    choice = gc.la1
                    # launch level 2
                elif event.key == K_F2:
                    maintain_home = 0
                    choice = gc.la2
    if choice != 0:
        # loading the background image
        background = pg.image.load(gc.background_picture).convert()

        # Generating a level from a file
        level = gl.Level(choice)
        level.generate()
        level.display(window)


        
