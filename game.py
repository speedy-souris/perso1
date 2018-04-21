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
from gamePack import game_function as functionality

""" window management
    Adaptation of the window according to the size of sprites
"""
pg.init()

# Initialization of window
window = pg.display.set_mode((constancy.window_size, 500))

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
    window.blit(menu, (0, 0))

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
            if event.type == QUIT or event.type == KEYDOWN and \
               event.key == K_ESCAPE:
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
        # loading the inventory part image (backpack, phial, needle, rod...)
        death = pg.image.load(constancy.death_picture).convert()
        empty = pg.image.load(constancy.empty_picture).convert()
        inventory = pg.image.load(constancy.inventory_picture).convert_alpha()
        backpack = pg.image.load(constancy.backpack).convert_alpha()
        phial = pg.image.load(constancy.phial).convert_alpha()
        needle = pg.image.load(constancy.needle).convert_alpha()
        rod = pg.image.load(constancy.rod).convert_alpha()

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
                # q key to quit the game after the death of persona 'MacGyver'
                elif event.key == K_q:
                    maintain_game = 0
                    maintain = 0
                # Button for moving the persona
                elif event.key == K_RIGHT:
                    mg.move('right')
                elif event.key == K_LEFT:
                    mg.move('left')
                elif event.key == K_UP:
                    mg.move('up')
                elif event.key == K_DOWN:
                    mg.move('down')

        window.blit(inventory, (0, 450))
        window.blit(background, (0, 0))
        window.blit(backpack, (160, 460))
        level.display(window)
        window.blit(mg.direction, (mg.x, mg.y))
        pg.display.flip()

        """
        Item Recovery
        """
        if level.framework[mg.case_y][mg.case_x] == 'p':  # phial recovery
            window.blit(phial, (195, 460))
            functionality.delete(level.framework, 'p')

        if level.framework[mg.case_y][mg.case_x] == 'l':  # needle recovery
            window.blit(needle, (230, 460))
            functionality.delete(level.framework, 'l')

        if level.framework[mg.case_y][mg.case_x] == 'r':  # rod recovery
            window.blit(rod, (265, 460))
            functionality.delete(level.framework, 'r')

        if level.framework[mg.case_y][mg.case_x] == "o":
            if shape.Level.backpack == 3:
                window.blit(empty, (195, 460))
                window.blit(empty, (230, 460))
                window.blit(empty, (265, 460))
                shape.Level.backpack = 0
                maintain_game = 0
            else:
                shape.Level.backpack < 3
                window.blit(death, (0, 450))
