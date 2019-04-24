# Names: Emmanuel Ogunjirin | AJ Given
# Computing ID: EAO5XC | AJG3QC

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# This game project was designed as an assignment for the Introductory to Computer Engineering (CS-1111) course.
# This game consists of a collection of games put that was designed and created by the names listed above for the final game project of the class.

import pygame       # Gets the pygame library
import gamebox      # Gets the gamebox library

width = 800     # Sets the width to the size
height = 600        # Sets the height to the size.
camera = gamebox.Camera(width, height)       # This is the camera that pans the screen.

main_screen_character = gamebox.from_circle(width / 2, height / 2, 'white', 10)      # This is the main screen character.
main_screen_character_speed = 10        # This is the speed of the white bob.

square_width = 50       # This is how wide the squares are
square_height = 50      # This is how high the squares are
first_square_spacing = 400      # This is where the first squares are and the others are based off this one.

snakeOption = gamebox.from_color(width / 3, height - first_square_spacing, 'green', square_width, square_height)       # Snake game
asteroidsOption = gamebox.from_color(width - width / 3, height - first_square_spacing, 'red', square_width, square_height)     # Asteroid game
bricksOption = gamebox.from_color(width / 3, height - first_square_spacing + 150, 'blue', square_width, square_height)       # Bricks game
flappybirdOption = gamebox.from_color(width - width / 3, height - first_square_spacing + 150, 'yellow', square_width, square_height)    # Flappy bird game
tronOption = gamebox.from_color(width / 3, height - first_square_spacing + 300, 'orange', square_width, square_height)   # Tron game
pongOption = gamebox.from_color(width - width / 3, height - first_square_spacing + 300, 'magenta', square_width, square_height)      # Pong game

main_screen_things = \
    [
        # --------------------------------- These are the main screen instructions ---------------------------------- #
        gamebox.from_text(width / 2, 50, "!!! WELCOME !!!", 50, 'white', True),       # Instruction 1
        gamebox.from_text(width / 2, 100, "Use keyboard arrows, or 'A,W,S,D' keys. Move the white circle to desired game", 25, 'white', True),     # Instruction 2
        gamebox.from_text(width / 2, 125, "At any point in an active game, press 'E' to return to main screen.", 25, 'white', True, True),       # Instruction 3
        gamebox.from_text(width / 2, 150, "Developed by Emmanuel Ogunjirin (eao5xc) and AJ Givens (ajg3qc)", 25, 'white', True, True),  # Instruction 4

        # --------------------------------- These are the games ---------------------------------- #
        gamebox.from_text(width / 3, height - first_square_spacing + 50, "Snake", 25, 'green', True),        # This is the snake game
        gamebox.from_text(width / 3, height - first_square_spacing + 200, "Bricks", 25, 'blue', True),        # This is the bricks game
        gamebox.from_text(width / 3, height - first_square_spacing + 350, "Tron", 25, 'orange', True),          # This is the tron game
        gamebox.from_text(width - width / 3, height - first_square_spacing + 50, "Asteroids", 25, 'red', True),          # This is the asteroids game
        gamebox.from_text(width - width / 3, height - first_square_spacing + 200, "Flappy Bird", 25, 'yellow', True),         # This is the flappybird game
        gamebox.from_text(width - width / 3, height - first_square_spacing + 350, "Pong", 25, 'magenta', True)          # This is the pong game
    ]


games = \
    [
        snakeOption,        # This is the snake option on the screen
        asteroidsOption,        # This is the asteroid option on the screen
        bricksOption,       # This is the bricks option on the screen
        flappybirdOption,      # This is the flappy_bird option on the screen
        tronOption,     # This is the unknown1 option on the screen
        pongOption,     # This is the unknown2 option on the screen
    ]


def main_activity(keys):
    """
    Allows the user to pick from the available games which one they would like to play.
    :param keys:  A fun little picker is provided for fun.
    :return: Nothing, just runs the desired game.
    """
    camera.clear('black')       # Gets the dark background of the game platform.

    if pygame.K_LEFT in keys or pygame.K_a in keys:     # Gets the desired keys
        main_screen_character.x -= main_screen_character_speed       # move main_screen_character left
    if pygame.K_RIGHT in keys or pygame.K_d in keys:     # Gets the desired keys
        main_screen_character.x += main_screen_character_speed       # move main_screen_character right
    if pygame.K_UP in keys or pygame.K_w in keys:     # Gets the desired keys
        main_screen_character.y -= main_screen_character_speed       # move main_screen_character up
    if pygame.K_DOWN in keys or pygame.K_s in keys:     # Gets the desired keys
        main_screen_character.y += main_screen_character_speed       # move main_screen_character down

    # if main_screen_character.touches(snakeOption):   # This is the snake game
    #     exec(open("snake.py").read(), globals())        # Runs the snake game
    #     quit()      # Kills current thread

    if main_screen_character.touches(asteroidsOption):  # This is the asteroid game
        exec(open("asteroids.py").read(), globals())        # Runs the asteroid game
        quit()      # kills current thread

    if main_screen_character.touches(bricksOption):       # This is the bricks game
        exec(open("bricks.py").read(), globals())         # Runs the bricks game
        quit()        # Kills current thread

    if main_screen_character.touches(flappybirdOption):     # This is the flappybird game
        exec(open("flappybird.py").read(), globals())       # Runs the flappy bird game
        quit()      # Kills the current thread

    if main_screen_character.touches(tronOption):       # This is the tron game
        exec(open("tron.py").read(), globals())         # Runs the tron game
        quit()      # Kills current thread

    if main_screen_character.touches(pongOption):       # This is the pong game
        exec(open("pong.py").read(), globals())         # Runs the pong game
        quit()      # Kills current thread

    main_screen_items = games + main_screen_things     # All the items on the screen are put into this variable.

    for item in main_screen_items:      # For every item put into the variable module, iterate over each one.
        camera.draw(item)       # Draw the game and wait

    camera.draw(main_screen_character)      # Draws the main character on the screen, this is the white circle.
    camera.display()        # Displays the screen.


gamebox.timer_loop(30, main_activity)       # Runs through the activity 30 times a second.
