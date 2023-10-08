# Import the random library
import random

# Import the modules that will be used in the game
import time
import math

# Define the constants for the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 10

# Define the classes that will be used in the game
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        # Draw the player
        fill(255, 0, 0)
        ellipse(self.x, self.y, 50, 50)

class Module:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self):
        # Draw the module
        fill(0, 255, 0)
        ellipse(self.x, self.y, 25, 25)

# Initialize the game
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
modules = []

# Start the game loop
while True:
    # Clear the screen
    background(0)

    # Update the player position
    player.move(0, -PLAYER_SPEED)

    # Create new modules
    for i in range(random.randint(1, 5)):
        modules.append(Module(random.randint(0, SCREEN_WIDTH), 0, random.randint(5, 10)))

    # Update the modules position
    for module in modules:
        module.move()

    # Check if the player collided with a module
    for module in modules:
        if player.x > module.x - 25 and player.x < module.x + 25 and player.y > module.y - 25 and player.y < module.y + 25:
            # The player collided with a module, so the game is over
            print("Game over!")
            break

    # Draw the player and modules
    player.draw()
    for module in modules:
        module.draw()

    # Wait for 1/60th of a second
    time.sleep(1 / 60)
