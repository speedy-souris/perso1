"""
MacGyver's Labyrinth Game Class
"""
# Internal libraries
import random as rm
# external libraries
import pygame as pg
from pygame.locals import *
# local libraries
from gamePack import game_constant as constancy
from gamePack import game_function as functionality

class Level:
    """class to create a level"""
    # initialization of the persona at the start of the game
    initial_x = 0
    initial_y = 0
    # Initialization Level number
    level_number = 0


    def __init__(self, level_file):
        self.level_file = level_file
        self.framework = 0 # framework of labyrinth


    def generate(self):
        """Method for generating the level based on the file.
        We create a general list, containing a list by line to display"""
        # file opening
        with open(self.level_file, "r") as level_file:
            framework_level = []
            item_level = []
            # course of each line of the file
            for line in level_file:
                line_level = []
                line_item =[]
                # We go through the sprites (letters) contained in the file
                for sprite in line:
                    # We ignore the end of line "\ n"
                    if sprite != '\n':
                        # We add the sprite to the list of the line
                        line_level.append(sprite)
                # Add the line to the level list
                framework_level.append(line_level)

            # We safeguard this framework
            self.framework = framework_level
            functionality.random_position_phial(self.framework)
            functionality.random_position_needle(self.framework)
            functionality.random_position_rod(self.framework)

    def display(self, window):
        """Method for displaying the level according to
        the framework list returned by generate ()"""

        # Loading images (only the arrival one contains transparency)
        wall = pg.image.load(constancy.wall_picture).convert()
        starting = pg.image.load(constancy.starting_picture).convert()
        arrival = pg.image.load(constancy.arrival_picture).convert_alpha()
        # Initialization utensils of game
        phial = pg.image.load(constancy.phial).convert_alpha()
        needle = pg.image.load(constancy.needle).convert_alpha()
        rod = pg.image.load(constancy.rod).convert_alpha()

        # We go through the list of level
        number_line = 0
        for line in self.framework:
            # We go through the lists of lines
            number_case = 0
            for sprite in line:
                # The actual position in pixels is calculated
                x = number_case * constancy.sprite_size
                y = number_line * constancy.sprite_size
                if sprite == '#':            # # = Wall
                    window.blit(wall, (x,y))
                elif sprite == 'i':          # i = Starting
                    Level.initial_x = number_case
                    Level.initial_y = number_line
                    window.blit(starting, (x,y))
                    if y == 30:
                        Level.level_number = 1
                    elif y == 420:
                        Level.level_number = 2
                elif sprite == 'o':          # o = Arrival
                    window.blit(arrival, (x,y))
                elif sprite == 'p':          # p = phial
                    window.blit(phial, (x,y))
                elif sprite == 'l':          # l = needle
                    window.blit(needle, (x,y))
                elif sprite == 'r':          # r = rod
                    window.blit(rod, (x,y))
                number_case += 1
            number_line += 1





class Persona:
    """Class to create a sprite for each movement in the labyrinth."""
    def __init__(self, right, left, up, down, level):
        # persona's sprite
        self.right = pg.image.load(constancy.mg_right).convert_alpha()
        self.left = pg.image.load(constancy.mg_left).convert_alpha()
        self.up = pg.image.load(constancy.mg_up).convert_alpha()
        self.down = pg.image.load(constancy.mg_down).convert_alpha()

        #Position of the persona in boxes and pixels
        self.case_x = Level.initial_x
        self.case_y = Level.initial_y
        self.x = self.case_x * constancy.sprite_size
        self.y = self.case_y * constancy.sprite_size

        # Default direction
        self.direction = self.up
        # level in which the persona is located
        self.level = level


    def move(self, direction):
        """Method for moving the persona"""
        # Move to the right
        if direction == 'right':
            # Not to exceed the screen
            if self.case_x < (constancy.number_sprite-1):
                # We check that the destination box is not a wall
                if self.level.framework[self.case_y][self.case_x+1] != '#':
                    # Moving a box
                    self.case_x += 1
                    # Calculation of the "real" position in pixels
                    self.x = self.case_x * constancy.sprite_size

            # Image in the right direction
            self.direction = self.right

        # Move to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.framework[self.case_y][self.case_x-1] != '#':
                    self.case_x -= 1
                    self.x = self.case_x * constancy.sprite_size
            self.direction = self.left

        # Move to up
        if direction == 'up':
            if self.case_y > 0:
                if self.level.framework[self.case_y-1][self.case_x] != "#":
                    self.case_y -= 1
                    self.y = self.case_y * constancy.sprite_size
            self.direction = self.up

        # Move to down
        if direction == 'down':
            if self.case_y < (constancy.number_sprite-1):
                if self.level.framework[self.case_y+1][self.case_x] != '#':
                    self.case_y += 1
                    self.y = self.case_y * constancy.sprite_size
            self.direction = self.down
