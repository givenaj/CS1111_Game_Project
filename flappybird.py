# Names: Emmanuel Ogunjirin | AJ Givens
# Computing ID: EAO5XC | AJG3QC

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

import pygame       # Imports the pygame module
import gamebox      # Imports the gamebox module
import random       # Imports the random module

""" 
This is a flappybird like game made as an assignment for CS-1111 Game project. This project was done using the gamebox module developed by Professor Luther Tychonievich.
Other sources of help include google images where I acquired the images for the project and altered them to my fitting. This made the game look better :-)
"""

width = 800     # This is how wide the screen is
height = 600        # This is how tall the screen is

camera = gamebox.Camera(width, height)       # This is the camera that pans the screen.

bird_straight = 'http://drive.google.com/uc?export=view&id=1jNuB1HkF7KFI5z2BZ3DZ2lDDvktAgC2c'     # Normal bird view when not falling
bird_down = 'http://drive.google.com/uc?export=view&id=1f0dvy0JAq3q-CqvS1U8MgBZWoetbAt4l'   # Bird view when falling
obstacle_bottom = 'http://drive.google.com/uc?export=view&id=1JEC3kpyrVkw9pzZt40Lf5PHifYQRB0B1'      # This is the obstacle coming from the top.
obstacle_top = 'http://drive.google.com/uc?export=view&id=1AuHD1JOaQ4sLt_wqivfvWtL0J2SmnFxZ'     # This is the obstacle coming from the bottom
background = 'http://drive.google.com/uc?export=view&id=1uxUB5tClq-I3YgSRQ0bPzYZ95PBlT8Kt'       # This is the background image for the screen
fall_speed = 1      # This is how fast the bird falls ar first <---------------------- This value changes exponentially as the bird falls more.
obstacle_speed = -4     # This is how fast the game moves (negative to go in the opposite direction) <----------------- Change this value to alter the speed of the game.
obstacles_generation = 10       # This is how many obstacles are generated every 10 seconds of the game. (1 every seconds)
score_number = 0        # This is the score of the game <-------------------------- This value changes as more obstacles are avoided.
counter = 0     # This is a counter to generate more obstacles.
position = 800      # This is the position that the obstacle is made.

bird = bird_straight        # Initial making of the bird sprite.
bird_game = gamebox.from_image(width / 2, height / 2, bird)        # Gets the bird image from my folder
game_background = gamebox.from_image(0, 190, background)        # Gets the game background from my folder
game_background_start = gamebox.from_text(400, 200, 'Press Space to Start!', 60, 'blue', True)      # Instructions before start
game_score_instruction = gamebox.from_text(530, 50, ' <------ This is your score!', 30, 'yellow', False)        # Instructions before start
game_sprite_instruction = gamebox.from_text(230, 300, 'This is your character! ----> ', 30, 'red', False)   # Instructions before start
game_instruction = gamebox.from_text(400, 550, 'Press the space bar to fly, avoid hitting the poles, try to stay alive. Good luck!', 30, 'black', False)   # Instructions before start
game_over = gamebox.from_text(400, 250, "GAME OVER!", 50, "brown", True)        # Initializes the game over text for when it is called.
leave = gamebox.from_text(400, 350, 'Press "e" to leave the game', 20, "brown", False)  # Set the leave text

obstacles = []      # A running list of obstacles that is kept and reused.

game_on = False     # Sets the game to not start yet


def flappybird(keys):
    """
    This is the main function that runs the flappybird app. The function is run 30 times per second. This keeps the game going until the player loses.
    :return: Shows a score of the player based on the number of obstacles passed.
    """
    global fall_speed       # Accesses external fall speed.
    global bird_straight    # Accesses external sprite image
    global bird_down        # Accesses external sprite image
    global bird_game        # Accesses external sprite image made.
    global bird     # Accesses external sprite image variable.
    global counter      # Accesses the counter
    global score_number     # Accesses the score
    global obstacles        # Access tbe obstacles list
    global position     # Accesses the obstacle making position.
    global game_on      # Accesses the variable outside the function
    global leave        # Accesses the external variable

    camera.clear("white")       # Clears the screen so that it can be painted on newly.

    score = gamebox.from_text(400, 50, str(int(score_number)), 50, "yellow", True)      # Sets the score position for the number of obstacles avoided.
    game_over_end = gamebox.from_text(400, 300, "Score: " + str(int(score_number)), 40, 'brown', True)      # This is the position for the game over score item.

    if pygame.K_SPACE in keys:      # If the space bar is clicked
        game_on = True      # Start the game

    if game_on:       # If they started the game
        counter += 1        # Counter for the obstacle.

        if counter % obstacles_generation == 0:     # When the counter divided by a number has no remainder
            num_obs = 1    # how many obs to be created
            for i in range(num_obs):        # For every obstacle to be created

                distance_apart = 150         # Ideal number is 150, the math needs it to be this, any other number will be weird.

                lower_bound = random.randint(-200, 200)     # Set the lower bound to be a random number

                if lower_bound < 0:     # If the lower bound is negative
                    upper_bound = 750 - (abs(lower_bound) + distance_apart)     # Set the upper bound accordingly
                else:   # If the lower bound is negative
                    upper_bound = 790 - abs(lower_bound - distance_apart)       # Set the lower bound accordingly

                top_obstacles = gamebox.from_image(position, lower_bound, obstacle_top)      # Make the top obstacle.
                bottom_obstacles = gamebox.from_image(position, upper_bound, obstacle_bottom)       # Make the bottom obstacle.

                obstacles.append(top_obstacles)       # Append the top obstacle.
                obstacles.append(bottom_obstacles)            # Append the bottom obstacle.

                position += 200     # Set the position to increase by 200.

        camera.draw(game_background)        # Draw the background for the game.

        if pygame.K_SPACE in keys:      # If the user hits the space bar
            width_game = bird_game.x        # Set the width of the game to be the width of position of the bird image
            height_game = bird_game.y       # Set the height of the game to be the height of the position of the bird image
            bird = bird_straight        # Draw the bird in the normal position
            bird_game = gamebox.from_image(width_game, height_game, bird)  # Gets the bird image from my folder
            bird_game.y -= 50       # Set the bird to fly 50 pixels higher than it was before.
            fall_speed = 1      # Reset the fall speed.
            keys.remove(pygame.K_SPACE)     # Stop the key from being pressed down.

        elif pygame.K_UP in keys:      # If the user hits the up arrow
            width_game = bird_game.x        # Set the width of the game to be the width of position of the bird image
            height_game = bird_game.y       # Set the height of the game to be the height of the position of the bird image
            bird = bird_straight        # Draw the bird in the normal position
            bird_game = gamebox.from_image(width_game, height_game, bird)  # Gets the bird image from my folder
            bird_game.y -= 50       # Set the bird to fly 50 pixels higher than it was before.
            fall_speed = 1      # Reset the fall speed.
            keys.remove(pygame.K_UP)     # Stop the key from being pressed down.

        elif pygame.K_w in keys:      # If the user hits the w key
            width_game = bird_game.x        # Set the width of the game to be the width of position of the bird image
            height_game = bird_game.y       # Set the height of the game to be the height of the position of the bird image
            bird = bird_straight        # Draw the bird in the normal position
            bird_game = gamebox.from_image(width_game, height_game, bird)  # Gets the bird image from my folder
            bird_game.y -= 50       # Set the bird to fly 50 pixels higher than it was before.
            fall_speed = 1      # Reset the fall speed.
            keys.remove(pygame.K_w)     # Stop the key from being pressed down.

        else:       # If no appropriate keys are being pressed
            width_game = bird_game.x        # Set the width of the game to be the width of position of the bird image
            height_game = bird_game.y       # Set the height of the game to be the height of the position of the bird image

            bird = bird_down        # Set the bird image to be the bird down image.
            bird_game = gamebox.from_image(width_game, height_game, bird)  # Gets the bird image from my folder

            if fall_speed+1 >= fall_speed:      # If the next fall speed is greater than the current one
                bird_game.y += fall_speed       # Set the bird speed to be equal to the fall speed
                fall_speed += 1     # Then increment the fall speed to provide a faster falling rate.

        if pygame.K_e in keys:  # Sets the key to do the following action.
            exec(open("Game_Project.py").read(), globals())  # Returns to the main screen
            quit()  # Quits the game.

        for obstacle in obstacles:      # For every obstacle in the game
            obstacle.x += obstacle_speed        # The x position of the obstacle is incremented by the speed the obstacle is to move in
            camera.draw(obstacle)       # Draw the obstacle.

            if obstacle.x == score.x:       # For every obstacle that is equal to the position of the sprite bird
                score_number += 0.5     # Increment the score by half (The 30 times per second screen compensates for the other half to make it one)

            if bird_game.touches(obstacle) or 0 >= bird_game.y or bird_game.y >= height:        # If the bird touches an obstacle or touches the bottom of the screen
                if pygame.K_SPACE in keys:  # If the user hits the space bar
                    keys.remove(pygame.K_SPACE)  # Stop the key from being pressed down.

                score = gamebox.from_text(-100, -100, str(int(score_number)), 50, "yellow", False)      # Set the score to be the current score
                camera.draw(obstacle)       # Draw the obstacle
                camera.draw(bird_game)      # Draw the bird sprite
                camera.draw(game_over)      # Draw the game over screen
                camera.draw(game_over_end)      # Draw the game over score
                camera.draw(leave)      # Leaves the game
                camera.display()        # Display the images

                gamebox.timer_loop(3, flappybird)       # Slows down the screen so that they cannot play the game any more.

    else:   # If the game has not been started
        camera.draw(game_background)        # Show the background
        camera.draw(game_instruction)       # Instructions before start
        camera.draw(game_score_instruction)     # Instructions before start
        camera.draw(game_sprite_instruction)    # Instructions before start
        camera.draw(game_background_start)      # Instructions before start

    camera.draw(score)      # Draw the score
    camera.draw(bird_game)      # Draw the bird
    camera.display()        # Display the game


gamebox.timer_loop(30, flappybird)      # Calls the flappybird loop 30 times every second.
