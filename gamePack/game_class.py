"""
MacGyver's Labyrinth Game Class
"""
# external libraries
import pygame as pg
from pygame.locals import *

# local library
from gamePack.game_constant import *

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
        wall = pg.image.load(wall_picture).convert()
        starting = pg.image.load(starting_picture).convert()
        arrival = pg.image.load(arrival_picture).convert_alpha()

        # We go through the list of level
        number_line = 0
        for line in self.framework:
            # We go through the lists of lines
            number_case = 0
            for sprite in line:
                # The actual position in pixels is calculated
                x = number_case * sprite_size
                y = number_line * sprite_size
                if sprite == '#':            # # = Wall
                    window.blit(wall, (x,y))
                elif sprite == 'i':          # i = Starting
                    window.blit(starting, (x,y))

                elif sprite == 'o':          # o = Arrival
                    window.blit(arrival, (x,y))
                number_case += 1
            number_line += 1

class Persona:
    """Class to create a character for each movement in the maze."""
    def __init__(self, right, left, up, down, level):
        # persona's sprite
        self.right = pg.image.load(mg_right).convert_alpha()
        self.left = pg.image.load(mg_left).convert_alpha()
        self.up = pg.image.load(mg_up).convert_alpha()
        self.down = pg.image.load(mg_down).convert_alpha()

        # level in which the persona is located
        self.level = level

        # Default direction
        self.direction = self.up

    def ininitial_position(self, level):
        """method of positioning the sprite on the sprite of start up
        according to the level of the game"""
        self.level = level

        if level == "la1":
            self.case_x = 0
            self.case_y = 1
            self.x = 0
            self.y = 30
        elif level == "la2":
            self.case_x = 0
            self.case_y = 14
            self.x = 0
            self.y = 420




    def move(self, direction):
        """Method for moving the persona"""
        # Move to the right
        if direction == 'right':
            # Not to exceed the screen
            if self.case_x < (number_sprite-1):
                # We check that the destination box is not a wall
                if self.level.framework[self.case_y][self.case_x+1] != '#':
                    # Moving a box
                    self.case_x += 1
                    # Calculation of the "real" position in pixels
                    self.x = self.case_x * sprite_size

            # Image in the right direction
            self.direction = self.right

        # Move to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.framework[self.case_y][self.case_x-1] != '#':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size
            self.direction = self.left

        # Move to up
        if direction == 'up':
            if self.case_y > 0:
                if self.level.framework[self.case_y-1][self.case_x] != "#":
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size
            self.direction = self.up

        # Move to down
        if direction == 'down':
            if self.case_y < (number_sprite -1):
                if self.level.framework[self.case_y+1][self.case_x] != '#':
                    self.case_y += 1
                    self.y = self.case_y * sprite_size
            self.direction = self.down
