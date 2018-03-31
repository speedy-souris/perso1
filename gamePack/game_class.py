"""
MacGyver's Labyrinth Game Class
"""
# external libraries
import pygame as pg
from pygame.locals import *

# local library
from gamePack import game_constant as gc

class Level:
    """class to create a level"""
    def __init__(self, level_file):
        self.level_file = level_file
        self.framework = 0

    def generate(self):
        """Method for generating the level based on the file.
        We create a general list, containing a list by line to display"""
        # file opening
        with open(self.level_file, "r") as level_file:
            framework_level = []
            # course of each line of the file
            for line in level_file:
                line_level = []
                # We go through the sprites (letters) contained in the file
                for sprite in line:
                    # We ignore the end of line "\ n"
                    if sprite != '\n':
                        # We add the sprite to the list of the line
                        line_level.append(sprite)
                #Add the line to the level list
                framework_level.append(line_level)
            # We safeguard this framework
            self.framework = framework_level

    def display(self, window):
        """Method for displaying the level according to
        the framework list returned by generate ()"""
        # Loading images (only the arrival one contains transparency)
        wall = pg.image.load(gc.wall_picture).convert()
        starting = pg.image.load(gc.starting_picture).convert()
        arrival = pg.image.load(gc.arrival_picture).convert_alpha()

        # We go through the list of level
        number_line = 0
        for line in self.framework:
            # We go through the lists of lines
            number_case = 0
            for sprite in line:
                # The actual position in pixels is calculated
                x = number_case * gc.sprite_size
                y = number_line * gc.sprite_size
                if sprite == '#':            # # = Wall
                    window.blit(wall, (x,y))
                elif sprite == 'i':          # i = Starting
                    window.blit(starting, (x,y))
                elif sprite == 'o':          # o = Arrival
                    window.blit(arrival, (x,y))
                number_case += 1
            number_line += 1
