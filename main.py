# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    black = pygame.Color(0,0,0)
    # Frame rate control
    clock = pygame.time.Clock()
    dt = 0

    # Main Loop

    while True:
        # Makes close window work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        # Updates window
        screen.fill(black)
        pygame.display.flip()

        # Controls Framerate and recalculates frame delta
        dt = clock.tick(60) / 1000

    """
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    """


if __name__ == "__main__":
    main()