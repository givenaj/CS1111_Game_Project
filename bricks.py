# Names: Emmanuel Ogunjirin | AJ Givens
# Computing ID: EAO5XC | AJG3QC

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

import pygame       # Gets the pygame library
import gamebox      # Gets the gamebox library
import random       # Imports the random library

""" 
This is a bricks like game made as an assignment for CS-1111 Game project. This project was done using the gamebox module developed by Professor Luther Tychonievich.
This is the section of the game that runs a simple bricks game.
"""

width = 800     # This is the width of the screen
height = 600     # This is the height of the screen
camera = gamebox.Camera(width, height)       # Sets the camera to view in these many pixels

walls = \
    [
        gamebox.from_color(400, 600, "yellow", 1000, 20),       # This is the bottom wall on the screen
        gamebox.from_color(400, 0, "yellow", 1000, 20),         # This is the top wall on the screen
    ]


def bricks(keys):

    for wall in walls:  # For every wall in the game
        camera.draw(wall)       # Draws the wall for the game.

    camera.display()

gamebox.timer_loop(30, bricks)
