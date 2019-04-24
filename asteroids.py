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
This is a asteroid like game made as an assignment for CS-1111 Game project. This project was done using the gamebox module developed by Professor Luther Tychonievich.
This is the section of the game that runs a simple asteroid like game. The goal is to destroy the asteroids before they hit the Earth below. Use up your health and you die!!! 
"""

width = 800     # This is the width of the screen
height = 600     # This is the height of the scree
home_height = 100   # This is the height of the Earth used in the image.        <----------------------- Change this value accordingly.

counter = 0     # This is a counter used to generate enemies

shipSpeed = 10      # This is the speed of the spacecraft       <----------------------- Change this value accordingly.
bulletSpeed = -10       # This is the speed of the bullet fired     <----------------------- Change this value accordingly.
obstacleSpeed = 1       # This is the speed of the obstacles/enemies  <----------------------- Change this value accordingly.

kills = 0        # This is the score of the game    <-------------------------- This value changes as more obstacles are avoided.
health_home = 100       # This is the health of the earth in the game       <-------------------------- This value changes as more obstacles are not avoided.
health_ship = 100       # This is the health of the ship in the game        <-------------------------- This value changes as more obstacles are not avoided.

ship = 'http://drive.google.com/uc?export=view&id=1njCSHcm5PwFbM5tdaF1Eq0BRfTMNs7rr'        # This is where the ship image is called from.

camera = gamebox.Camera(width, height)       # Sets the camera to view in these many pixels
spaceShip = gamebox.from_image(width / 2, height - 100, ship)        # Gets the spaceship image from professor Upsorn's website.
game_over = gamebox.from_text(width / 2, height / 2 - 100, "GAME OVER!", 80, "yellow", True)        # Initializes the game over text for when it is called.

game_instruction = gamebox.from_text(width / 2, height / 2 - 100, "Press Space to Start!", 80, "purple", True)        # Initializes the game instructions
game_instruction1 = gamebox.from_text(width / 2, height / 2 - 30, "Press space to shoot, do NOT rapid fire", 30, "white", False)        # Initializes the game instructions
game_instruction2 = gamebox.from_text(width / 2, height / 2, "Avoid the blocks hitting you and the Earth", 30, "white", False) # Initializes the game instructions
game_instruction3 = gamebox.from_text(width / 2, height / 2 + 30, "!!! Destroy with extreme prejudice !!!", 30, "white", False) # Initializes the game instructions
game_person = gamebox.from_text(300, height - 100, "This is you ----->", 30, "white", False)        # Instructions 1
game_person1 = gamebox.from_text(width / 2, height - 150, "Control with arrows or 'ASWD' keys", 30, "white", False)    # Instructions 2
game_score = gamebox.from_text(150, 85, "This is your score", 30, "white", False)
person_health = gamebox.from_text(550, 85, "This is your health", 30, "white", False)
earth_health = gamebox.from_text(700, height - 65, "Earth", 30, "white", False)

obstacles = []      # This is a running list of the obstacles.
bullets = []        # This is a running list of the bullets.

game_on = False     # Sets the code to hold until started manually.


def asteroids(keys):
    """
    This is the main function that runs the asteroid app. The function is run 30 times per second. This keeps the game going until the player loses.
    :param keys: The user can use the 'A,W,S,D keys or the arrows to control the ship, press space bar to shoot, and press E/Esc to leave the game.
    :return: Provides the user with their score as well as the health lost at the end of the game.
    """
    global counter      # Accesses external counter.
    global kills        # Accesses external kill count.
    global home_height      # Accesses external home height.
    global health_ship  # Accesses external ship health.
    global health_home  # Accesses external home health.
    global bullet_item  # Accesses external bullet list.
    global game_on      # Accesses the variable outside the function

    counter += 1        # Increments the counter

    camera.clear('black')       # Gets the dark background of the game platform.

    bullet_item = gamebox.from_color(-300, 300, 'cyan', 5, 30)      # Makes the bullet
    home = gamebox.from_color(0, height, 'green', width * 2, 100)  # This is the earth image.
    score = gamebox.from_text(150, 50, 'Score: ' + str(int(kills)), 50, "yellow", True)      # Sets the score position for the number of obstacles avoided.
    ship_health_level = gamebox.from_text(width - width / 3, 50, 'Spaceship Health: ' + str(int(health_ship)), 50, 'yellow', True)        # Sets the health of the ship
    earth_health_level = gamebox.from_text(width / 2, 580, 'Earth Health: ' + str(int(health_home)), 50, 'yellow', True)      # Sets the health of the earth

    if pygame.K_SPACE in keys:      # If the space bar is clicked
        game_on = True      # Start the game

    if game_on:       # If they started the game
        if counter % 60 == 0:       # Runs the counter
            num_obstacles = random.randint(0, 8)    # how many enemies to be created
            for i in range(num_obstacles):      # For every enemy
                obstacles.append(gamebox.from_color(random.randrange(20, 780), 0, 'red', 20, 20))       # Append it to the obstacles list.

        if pygame.K_LEFT in keys or pygame.K_a in keys:     # Sets the key to do the following action
            spaceShip.x -= shipSpeed       # move spaceShip left
        if pygame.K_RIGHT in keys or pygame.K_d in keys:    # Sets the key to do the following action
            spaceShip.x += shipSpeed       # move spaceShip right
        if pygame.K_UP in keys or pygame.K_w in keys:       # Sets the key to do the following action
            spaceShip.y -= shipSpeed       # move spaceShip up
        if pygame.K_DOWN in keys or pygame.K_s in keys:     # Sets the key to do the following action
            spaceShip.y += shipSpeed       # move spaceShip down
        if pygame.K_e in keys:      # Sets the key to do the following action.
            exec(open("Game_Project.py").read(), globals())     # Returns to the main screen
            quit()      # Quits the game.
        if pygame.K_SPACE in keys:      # If the space bar is pressed
            bullets.append(bullet_item)     # Append a bullet to the bullet list.
            bullets[-1].speedy = bulletSpeed        # Set the speed
            bullets[-1].center = spaceShip.center   # Set the heading, and fire
            keys.remove(pygame.K_SPACE)     # Remove constantly fire capabilities.

        if spaceShip.x > width:     # If the ship is off the left side of the screen
            spaceShip.x = 0     # Move the ship back to the right
        if spaceShip.x < 0:     # If the ship is at the right side of the screen
            spaceShip.x = width     # Move the ship to the left
        if spaceShip.y > height - 85:       # If the ship is at the bottom of the screen where the earth is
            spaceShip.y = height - 85       # Stop it right there
        if spaceShip.y < 100:       # If the ship is at the top where the scores are
            spaceShip.y = 100       # Stop it right there.

        for obstacle in obstacles:      # For every obstacle in the list
            obstacle.y += obstacleSpeed        # Move the obstacle down
            if obstacle.touches(home):      # If the obstacle touches the Earth
                health_home -= 10   # Subtract from the health of the Earth
                home_height -= 1       # Move the height of the home down
                obstacles.remove(obstacle)      # Remove the obstacle
                home = gamebox.from_color(0, height, 'green', width * 2, home_height)  # Move the Earth image in an animation.
            if obstacle.touches(spaceShip):     # If the obstacle touches the ship
                health_ship -= 5        # Reduce the health of the ship
                obstacles.remove(obstacle)      # Remove the obstacle
            camera.draw(obstacle)       # Draw the obstacle.

        for bullet in bullets:      # For every bullet in the list
            bullet.move_speed()     # Move the bullet
            for obstacle in obstacles:      # For all obstacles
                if bullet.touches(obstacle):        # If the bullet touches the obstacle
                    kills += 1      # Add one to the score of kills
                    obstacles.remove(obstacle)      # Remove the obstacles
            camera.draw(bullet)     # Draw the bullet

        if health_ship <= 10:       # If the health of the ship is less than 10
            health_alarm = gamebox.from_text(200, 100, 'MISSION CRITICAL', 50, 'magenta', True)     # Sound an alarm
            camera.draw(health_alarm)       # Draw the health alarm

        if health_home <= 20:       # If the Earth health is less than 20
            health_alarm_home = gamebox.from_text(600, 100, 'EARTH IS FALLING!', 50, 'magenta', True)       # Sound the alarm
            home = gamebox.from_color(0, height, 'red', width * 2, 100)  # Reset the Earth Image
            camera.draw(health_alarm_home)      # Draw the health alarm

    else:       # If the game has not been started
        camera.draw(game_instruction)       # Shows instructions
        camera.draw(game_instruction1)       # Shows instructions
        camera.draw(game_instruction2)       # Shows instructions
        camera.draw(game_instruction3)       # Shows instructions
        camera.draw(game_person)       # Shows instructions for the person
        camera.draw(game_person1)       # Shows instructions for the person
        camera.draw(person_health)       # Shows instructions for person health
        camera.draw(game_score)       # Shows instructions for score
        camera.draw(earth_health)       # Shows instructions for Earth health

    camera.draw(home)       # Draws the home on the screen, this should be green for earth.
    camera.draw(score)      # Show the score on the page
    camera.draw(ship_health_level)      # Show the ship health
    camera.draw(earth_health_level)     # Show the Earth health
    camera.draw(spaceShip)      # Draws the spaceShip on the screen, this is the white circle.

    if health_ship <= 0 or health_home <= 0:        # If either of the healths are 0
        obstacles.clear()       # Clears all obstacles coming.
        camera.clear('black')   # Clear the screen
        if health_home <= 0:        # Alters the score
            health_home = 0     # Alters the score
        if health_ship <= 0:        # Alters the score
            health_ship = 0     # Alters the score
        ship_health_level = gamebox.from_text(width / 2, height / 2 + 50, 'Ship Health: ' + str(int(health_ship)), 50, 'yellow', True)      # Show the ship health
        home_health_level = gamebox.from_text(width / 2, height / 2 + 100, 'Earth Health: ' + str(int(health_home)), 50, 'yellow', True)    # Show the Earth health
        score = gamebox.from_text(width / 2, height / 2, 'Score: ' + str(int(kills)), 50, "yellow", True)   # Sets the score position for the number of obstacles avoided.
        leave = gamebox.from_text(width/2, height/2 + 150, 'Press "e" to leave the game', 30, "yellow", False)  # Set the leave text
        camera.draw(score)      # Draw the score
        camera.draw(leave)      # Leaves the game
        camera.draw(ship_health_level)      # Draw the Earth health
        camera.draw(home_health_level)      # Draw the home health
        camera.draw(game_over)      # Draw the Game Over text

    camera.display()        # Displays the screen


gamebox.timer_loop(30, asteroids)       # Loops through the code again 30 times per second.
