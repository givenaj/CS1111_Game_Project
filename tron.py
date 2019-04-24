# Names: Emmanuel Ogunjirin | AJ Givens
# Computing ID: EAO5XC | AJG3QC

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

import pygame       # Gets the pygame library
import gamebox      # Gets the gamebox library

""" 
This is a Tron like game made as an assignment for CS-1111 Game Project. This project was done using the gamebox module developed by Professor Luther Tychonievich.
This is the classic Tron game - Try to corner your opponent into hitting you while trying not to hit them :-) 
"""

width = 800     # This is the width of the window
height = 600    # This is the height of the window

camera = gamebox.Camera(width, height)      # Draws the window

redPlayer = gamebox.from_circle(750, 550, 'red', 5)     # This is the red player
bluePlayer = gamebox.from_circle(50, 50, 'blue', 5)     # This is the blue player

redPlayer_instruction = gamebox.from_text(600, 550, 'This is the red player ---> ', 30, 'red', False)             # Draws Instructions
bluePlayer_instruction = gamebox.from_text(250, 50, '<--- This is the blue player', 30, 'blue', False)      # Draws Instructions
redPlayer_instruction1 = gamebox.from_text(400, 500, 'Use the arrows to control the red player', 30, 'red', False)      # Draws Instructions
bluePlayer_instruction1 = gamebox.from_text(400, 100, 'Use the "A,W,S,D" keys to control the blue player', 30, 'blue', False)      # Draws Instructions
general_instructions = gamebox.from_text(400, 300, 'Press Space to Start!', 80, 'white', True)      # Draws Instructions
general_instructions1 = gamebox.from_text(400, 350, 'Try to make your opponent hit you', 40, 'white', True)      # Draws Instructions

redPlayerPositions = []     # Keeps a running list of the position of the red player
bluePlayerPositions = []    # Keeps a running list of the position of the blue player

game_on = False     # Freezes the screen to begin
number = 0      # Sets the start to 0


def tron(keys):
    """
    This is the main function that runs the tron app. The function is run 30 times per second. This keeps the game going until the player loses.
    :param keys: The players are controlled by the 'A,W,S,D' keys for th blue player, and the arrow keys for the red player.
    :return:  Shows who wins the game at the end of the run
    """
    global game_on      # Accesses the outside game
    global number       # Accesses the outside variable.

    if pygame.K_SPACE in keys:      # If the space bar is pressed
        camera.clear('black')       # Clears the screen once unless pressed again.
        game_on = True      # Start the game

    if game_on:     # When the game is started
        if pygame.K_LEFT in keys:     # Sets the key to do the following action
            redPlayer.x -= 5       # move redPlayer left
        if pygame.K_RIGHT in keys:        # Sets the key to do the following action
            redPlayer.x += 5       # move redPlayer right
        if pygame.K_UP in keys:       # Sets the key to do the following action
            redPlayer.y -= 5       # move redPlayer up
        if pygame.K_DOWN in keys:     # Sets the key to do the following action
            redPlayer.y += 5       # move redPlayer down

        if pygame.K_a in keys:     # Sets the key to do the following action
            bluePlayer.x -= 5       # move bluePlayer left
        if pygame.K_d in keys:        # Sets the key to do the following action
            bluePlayer.x += 5       # move bluePlayer right
        if pygame.K_w in keys:       # Sets the key to do the following action
            bluePlayer.y -= 5       # move bluePlayer up
        if pygame.K_s in keys:     # Sets the key to do the following action
            bluePlayer.y += 5       # move bluePlayer down
        if pygame.K_e in keys:      # Sets the key to do the following action.
            exec(open("Game_Project.py").read(), globals())     # Returns to the main screen
            quit()      # Quits the game.

        if redPlayer.x > width:     # If the ship is off the left side of the screen
            redPlayer.x = 0     # Move the ship back to the right
        if redPlayer.x < 0:     # If the ship is at the right side of the screen
            redPlayer.x = width     # Move the ship to the left
        if redPlayer.y > height:       # If the player is at the bottom of the screen
            redPlayer.y = 0       # Moves it back to the top of the screen
        if redPlayer.y < 0:       # If the player is at the top
            redPlayer.y = height       # Moves it back to the top of the screen

        if bluePlayer.x > width:     # If the ship is off the left side of the screen
            bluePlayer.x = 0     # Move the ship back to the right
        if bluePlayer.x < 0:     # If the ship is at the right side of the screen
            bluePlayer.x = width     # Move the ship to the left
        if bluePlayer.y > height:       # If the player is at the bottom of the screen
            bluePlayer.y = 0       # Moves it back to the top of the screen
        if bluePlayer.y < 0:       # If the player is at the top
            bluePlayer.y = height       # Moves it back to the top of the screen

        redplayerposition = [redPlayer.x, redPlayer.y]      # Gets the coordinate of the red player position
        blueplayerposition = [bluePlayer.x, bluePlayer.y]       # Gets the coordinate of the blue player position

        redPlayerPositions.append(redplayerposition)        # Appends the coordinate to the red player list.
        bluePlayerPositions.append(blueplayerposition)      # Appends the coordinate to the blue player list.

        for redposition in redPlayerPositions:      # For every position in the red player path
            if bluePlayerPositions[len(bluePlayerPositions) - 1] == redposition:        # If the blue player current position is in that position
                winner = gamebox.from_text(width / 2, height / 2, 'RED WINS!', 80, 'red', True)      # The winner is the red player
                camera.draw(winner)     # Draw the winner
                camera.draw(gamebox.from_text(width/2, height/2 + 100, 'Press "e" to leave the game', 30, 'red', False))      # This is the instruction for leaving the game

        for blueposition in bluePlayerPositions:        # For every position in the blue player path
            if redPlayerPositions[len(redPlayerPositions) - 1] == blueposition:        # If the red player current position is in that position
                winner = gamebox.from_text(width / 2, height / 2, 'BLUE WINS!', 80, 'blue', True)      # The winner is the blue player
                camera.draw(winner)     # Draw the winner
                camera.draw(gamebox.from_text(width / 2, height / 2 + 100, 'Press "e" to leave the game', 30, 'blue', False))  # This is the instruction for leaving the game

    else:
        camera.draw(redPlayer_instruction)      # Draws Instructions
        camera.draw(bluePlayer_instruction)      # Draws Instructions
        camera.draw(redPlayer_instruction1)      # Draws Instructions
        camera.draw(bluePlayer_instruction1)      # Draws Instructions
        camera.draw(general_instructions)      # Draws Instructions
        camera.draw(general_instructions1)      # Draws Instructions

    camera.draw(bluePlayer)     # Draw the blue player
    camera.draw(redPlayer)      # Draw the red player

    camera.display()  # Displays the screen


gamebox.timer_loop(30, tron)  # Loops through the code again 30 times per second.
