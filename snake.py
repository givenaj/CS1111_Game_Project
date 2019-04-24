# Names: Emmanuel Ogunjirin | AJ Givens
# Computing ID: EAO5XC | (Insert AJ Given's Computing ID here

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

import pygame       # Gets the pygame library
import gamebox

""" This is the classic snake game - Eat as many apples as you can without hitting/eating yourself :-) """

camera = gamebox.Camera(800, 600)
snakeItem = gamebox.from_circle(400, 400, 'white', 5)


def snake(keys):
    """
    ....
    :param keys:
    :return:
    """
    camera.clear('black')       # Gets the dark background of the game platform.

    if pygame.K_LEFT in keys or pygame.K_a in keys:     # Sets the key to do the following action
        snakeItem.x -= 5       # move snakeItem left
    if pygame.K_RIGHT in keys or pygame.K_d in keys:        # Sets the key to do the following action
        snakeItem.x += 5       # move snakeItem right
    if pygame.K_UP in keys or pygame.K_w in keys:       # Sets the key to do the following action
        snakeItem.y -= 5       # move snakeItem up
    if pygame.K_DOWN in keys or pygame.K_s in keys:     # Sets the key to do the following action
        snakeItem.y += 5       # move snakeItem down
    if pygame.K_e in keys:  # Sets the key to do the following action.
        exec(open("Game_Project.py").read(), globals())  # Returns to the main screen
        quit()  # Quits the game.

    camera.draw(snakeItem)      # Draws the main character on the screen, this is the white circle.

    camera.display()            # Displays the screen


gamebox.timer_loop(30, snake)       # Loops through the code again 30 times per second.
