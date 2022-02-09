# goal of the game is to avoid incoming obstacles
# player can move in all cardinal directions (left, right, top, bottom)
# player cannot move off the screen
# if the player hits an obstacle, then the game ends
import pygame
from pygame import *
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

width = 800
height = 600


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, keys_pressed):
        if keys_pressed[K_UP]:
            self.rect.move_ip(0, -1)
            self.surf.fill((random.randint(250, 255), random.randint(250, 255), random.randint(250, 255)))
        if keys_pressed[K_DOWN]:
            self.rect.move_ip(0, 1)
            self.surf.fill((random.randint(250, 255), random.randint(250, 255), random.randint(250, 255)))
        if keys_pressed[K_LEFT]:
            self.rect.move_ip(-1, 0)
            self.surf.fill((random.randint(250, 255), random.randint(250, 255), random.randint(250, 255)))
        if keys_pressed[K_RIGHT]:
            self.rect.move_ip(1, 0)
            self.surf.fill((random.randint(250, 255), random.randint(250, 255), random.randint(250, 255)))

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom = height


on = True

pygame.init()

screen = pygame.display.set_mode((width, height))
player = Player()

# Main loop
while on:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                on = False

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            on = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()
