# Names: Emmanuel Ogunjirin | AJ Givens
# Computing ID: EAO5XC | AJG3QC

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

import pygame       # Gets the pygame library
import gamebox
import random       # Imports the random module

""" 
This is a Pong like game made as an assignment for CS-1111 Game Project. This project was done using the gamebox module developed by Professor Luther Tychonievich.
This is the classic Pong game - Try to score more than your opponent :-) 
"""

width = 800     # This is the width of the screen
height = 600        # This is the height of the screen

camera = gamebox.Camera(width, height)      # This is the screen shown
number = random.randint(0, 4)       # A random number between 1-4 is chosen

p_width = 10        # The player width
p_height = 80       # The player heights
ball_velocity = 15      # The ball velocity
player_speed = 15       # The player speeds
red_score = 0       # The score for the red team
green_score = 0     # The score for the green team
game_on = False     # The game status
numberLimit = 10        # The limit of the game     <------------------- This is the max score of the game

walls = \
    [
        gamebox.from_color(400, 600, "yellow", 1000, 20),       # This is the bottom wall on the screen
        gamebox.from_color(400, 0, "yellow", 1000, 20),         # This is the top wall on the screen
    ]

redPlayer = gamebox.from_color(20, height / 2, "red", 15, 100)        # This is the red player
greenPlayer = gamebox.from_color(780, height / 2, "green", 15, 100)       # This is the green player
ball = gamebox.from_color(400, 300, "yellow", 20, 20)       # This is the ball

ball.xspeed = ball_velocity     # This is the ball speed in the x direction
ball.yspeed = ball_velocity     # This is the ball speed in the y direction

instruction = gamebox.from_text(400, 200, 'Press Space to Start!', 80, 'purple', True)      # This is the instruction
instruction1 = gamebox.from_text(400, 500, '! Prevent the ball from scoring on your side !', 40, 'yellow', False)      # This is the instruction
instruction2 = gamebox.from_text(400, 550, '!! First to ' + str(numberLimit) + ' wins the game !!', 40, 'yellow', False)      # This is the instruction
redInstructions = gamebox.from_text(170, height / 2, '<-- Control with "W,S" Keys', 30, 'red', False)      # This is the instruction for the player
greenInstructions = gamebox.from_text(650, height / 2, 'Control with arrows -->', 30, 'green', False)      # This is the instruction for the player
redScore = gamebox.from_text(200, 50, 'Red Score ----> ', 30, 'red', False)      # This is the instruction for the score
greenScore = gamebox.from_text(610, 50, '<---- Green Score', 30, 'green', False)      # This is the instruction for the score
ballInstructions = gamebox.from_text(400, 330, 'This is the ball', 30, 'yellow', False)      # This is the instruction for the ball


def pong(keys):
    """
    This is the main function that runs the tron app. The function is run 30 times per second. This keeps the game going until the player loses.
    :param keys: The 'WD' keys control the red players, and the top and bottom arrows control the green player. The ball is random movement.
    :return: Gives a score of the winner in a specified round match
    """
    global game_on      # Gets the outside variable
    global red_score    # Gets the outside variable
    global green_score    # Gets the outside variable
    global number    # Gets the outside variable
    global numberLimit    # Gets the outside variable
    global ballInstructions    # Gets the outside variable
    global instruction    # Gets the outside variable
    global instruction1    # Gets the outside variable
    global instruction2    # Gets the outside variable
    global redInstructions    # Gets the outside variable
    global greenInstructions    # Gets the outside variable
    global redScore    # Gets the outside variable
    global greenScore    # Gets the outside variable

    camera.clear("black")       # Clears the camera

    if pygame.K_SPACE in keys:      # If the space bar is hit
        game_on = True      # Starts the game

    if game_on:     # When the game starts
        if number == 0:     # If the random number is 0
            ball.x += ball.xspeed       # Modify the direction accordingly
            ball.y += ball.yspeed       # Modify the direction accordingly
        elif number == 1:     # If the random number is 1
            ball.x -= ball.xspeed       # Modify the direction accordingly
            ball.y -= ball.yspeed       # Modify the direction accordingly
        elif number == 2:     # If the random number is 2
            ball.x += ball.xspeed       # Modify the direction accordingly
            ball.y -= ball.yspeed       # Modify the direction accordingly
        elif number == 3:     # If the random number is 3
            ball.x -= ball.xspeed       # Modify the direction accordingly
            ball.y += ball.yspeed       # Modify the direction accordingly
        else:
            number = random.randint(0, 4)     # Picks a random number and runs immediately.

        if pygame.K_UP in keys:       # Sets the key to do the following action
            greenPlayer.y -= player_speed       # move redPlayer up
        if pygame.K_DOWN in keys:     # Sets the key to do the following action
            greenPlayer.y += player_speed       # move redPlayer down

        if pygame.K_w in keys:       # Sets the key to do the following action
            redPlayer.y -= player_speed       # move bluePlayer up
        if pygame.K_s in keys:     # Sets the key to do the following action
            redPlayer.y += player_speed       # move bluePlayer down

        if pygame.K_e in keys:      # Sets the key to do the following action.
            exec(open("Game_Project.py").read(), globals())     # Returns to the main screen
            quit()      # Quits the game.

        for wall in walls:       # For every wall in the game
            if ball.touches(wall):      # If the ball touches the wall
                ball.yspeed *= -1       # Change the direction of the ball

        if ball.touches(redPlayer):     # If the ball touches the player
            ball.xspeed *= -1       # Change it's direction
        if ball.touches(greenPlayer):     # If the ball touches the player
            ball.xspeed *= -1       # Change it's direction

        if redPlayer.y >= height:       # If the player touches the bottom of the screen
            redPlayer.y = height        # Stop it
        if redPlayer.y <= 0:        # If the player touches the top of the screen
            redPlayer.y = 0     # Stop it.

        if greenPlayer.y >= height:       # If the player touches the bottom of the screen
            greenPlayer.y = height        # Stop it
        if greenPlayer.y <= 0:       # If the player touches the top of the screen
            greenPlayer.y = 0        # Stop it

        if ball.x >= width:     # If the ball passes past the green player
            red_score += 1      # Add one to the red score
            ball.x = width/2        # Move the ball back to the start position
            ball.y = height/2       # Move the ball back to the start position
            redPlayer.y = height/2      # Move the red player back to start position
            greenPlayer.y = height/2        # Move the green player back to start position
            game_on = False     # Set the game to false.

        if ball.x <= 0:     # If the ball passes past the green player
            green_score += 1      # Add one to the red score
            ball.x = width/2        # Move the ball back to the start position
            ball.y = height/2       # Move the ball back to the start position
            redPlayer.y = height/2      # Move the red player back to start position
            greenPlayer.y = height/2        # Move the green player back to start position
            game_on = False     # Set the game to false.

    else:
        camera.draw(instruction)        # Instructions before starting
        camera.draw(instruction1)        # Instructions before starting
        camera.draw(instruction2)        # Instructions before starting
        camera.draw(redInstructions)        # Instructions before starting
        camera.draw(greenInstructions)        # Instructions before starting
        camera.draw(redScore)        # Instructions before starting
        camera.draw(greenScore)        # Instructions before starting
        camera.draw(ballInstructions)        # Instructions before starting

    camera.draw(gamebox.from_text(300, 50, str(red_score), 50, "Red", bold=True))       # The red score
    camera.draw(gamebox.from_text(500, 50, str(green_score), 50, "green", bold=True))   # The green score

    for wall in walls:      # For every wall in the walls list
        camera.draw(wall)       # Draw the wall

    camera.draw(redPlayer)      # Draws the red player
    camera.draw(greenPlayer)        # Draws the green player
    camera.draw(ball)       # Draws the ball

    if 0 < red_score >= numberLimit:        # If the red score is 10 first
        ball.move(width/2, height/2)
        camera.draw(gamebox.from_text(width / 2, height / 2 + 50, "Red Wins!", 40, "Red", True))     # Print red wins
        ballInstructions = gamebox.from_text(width / 2, height / 2, 'Press "e" to leave the game', 30, 'yellow', False)      # This is the instruction for leaving the game
        instruction = gamebox.from_text(400, 200, '', 80, 'purple', True)  # This is the instruction
        instruction1 = gamebox.from_text(400, 500, '', 40, 'yellow', False)  # This is the instruction
        instruction2 = gamebox.from_text(400, 550, '', 40, 'yellow', False)  # This is the instruction
        redInstructions = gamebox.from_text(170, height / 2, '', 30, 'red', False)  # This is the instruction for the player
        greenInstructions = gamebox.from_text(650, height / 2, '', 30, 'green', False)  # This is the instruction for the player
        redScore = gamebox.from_text(200, 50, '', 30, 'red', False)  # This is the instruction for the score
        greenScore = gamebox.from_text(610, 50, '', 30, 'green', False)  # This is the instruction for the score

        if pygame.K_SPACE in keys:      # Sets the key to do the following action.
            exec(open("Game_Project.py").read(), globals())     # Returns to the main screen
            quit()      # Quits the game.

        if pygame.K_e in keys:      # Sets the key to do the following action.
            exec(open("Game_Project.py").read(), globals())     # Returns to the main screen
            quit()      # Quits the game.

    if 0 < green_score >= numberLimit:      # IF the green score is 10 first
        ball.move(width/2, height/2)        # Moves the ball to the specified coordinate
        camera.draw(gamebox.from_text(width / 2, height / 2 + 50, "Green Wins!", 40, "green", True))     # Print green wins
        ballInstructions = gamebox.from_text(width / 2, height / 2, 'Press "e" to leave the game', 30, 'yellow', False)      # This is the instruction for leaving the game
        instruction = gamebox.from_text(400, 200, '', 80, 'purple', True)  # This is the instruction
        instruction1 = gamebox.from_text(400, 500, '', 40, 'yellow', False)  # This is the instruction
        instruction2 = gamebox.from_text(400, 550, '', 40, 'yellow', False)  # This is the instruction
        redInstructions = gamebox.from_text(170, height / 2, '', 30, 'red', False)  # This is the instruction for the player
        greenInstructions = gamebox.from_text(650, height / 2, '', 30, 'green', False)  # This is the instruction for the player
        redScore = gamebox.from_text(200, 50, '', 30, 'red', False)  # This is the instruction for the score
        greenScore = gamebox.from_text(610, 50, '', 30, 'green', False)  # This is the instruction for the score

        if pygame.K_SPACE in keys:      # Sets the key to do the following actions
            exec(open("Game_Project.py").read(), globals())     # Returns to the main screen
            quit()      # Quits the game

        if pygame.K_e in keys:      # Sets the key to do the following action.
            exec(open("Game_Project.py").read(), globals())     # Returns to the main screen
            quit()      # Quits the game.

    camera.display()        # Displays the screen


gamebox.timer_loop(30, pong)        # Moves through the screen 30 times per second.
