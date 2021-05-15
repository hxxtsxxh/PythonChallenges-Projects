# creating a screen and showing a blue circle
import pygame
from pygame import *

pygame.init()
width = 500
height = 500

center_shape = (width/2, height/2)

# set up a window with dimensions
screen = pygame.display.set_mode([width, height])

# loop so the program runs until user quits
on = True
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    screen.fill((255, 255, 255)) # this is in rgb

    # draw a blue circle in the center
    # ((color), (location), radius)
    pygame.draw.circle(screen, (0, 0, 255), center_shape, 75)

    # Flip the display
    pygame.display.flip()

# Done. Time to quit.
pygame.quit()
