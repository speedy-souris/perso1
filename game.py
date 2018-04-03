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
from gamePack import game_constant as constancy
from gamePack import game_class as shape


""" window management
    Adaptation of the window according to the size of sprites
"""
pg.init()

# Initiation of window
window = pg.display.set_mode((constancy.window_size, constancy.window_size))

# icon of the window
icon = pg.image.load(constancy.window_icon)
pg.display.set_icon(icon)
# Title of the window
pg.display.set_caption(constancy.window_title)

"""
Main loop of the game
"""
maintain = 1
while maintain:
    # home menu display
    menu = pg.image.load(constancy.menu_picture).convert()
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
                    choice = constancy.la1
                    # launch level 2
                elif event.key == K_F2:
                    maintain_home = 0
                    choice = constancy.la2
    if choice != 0:
        # loading the background image
        background = pg.image.load(constancy.background_picture).convert()

        # Generating a level from a file
        level = shape.Level(choice)
        level.generate()
        level.display(window)


        # Creating macGyver (persona)
        mg = shape.Persona(constancy.mg_right, constancy.mg_left,
            constancy.mg_up, constancy.mg_down, level)

    """
    GAME LOOP
    """
    while maintain_game:
        for event in pg.event.get():
            # Close the window to quit
            if event.type == QUIT:
                maintain_game = 0
                maintain = 0
            # ESC key to return to the menu
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    maintain_game = 0
                # Button for moving the persona
                elif event.key == K_RIGHT:
                    mg.move('right')
                elif event.key == K_LEFT:
                    mg.move('left')
                elif event.key == K_UP:
                    mg.move('up')
                elif event.key == K_DOWN:
                    mg.move('down')

        window.blit(background,(0,0))
        level.display(window)
        window.blit(mg.direction,(mg.x,mg.y))
        pg.display.flip()

        if level.framework[mg.case_y][mg.case_x] == "o":
            maintain_game = 0
