# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    black = pygame.Color(0,0,0)
    
    # Frame rate control
    clock = pygame.time.Clock()
    dt = 0

    # Player
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    # Main Loop

    while True:
        # Makes close window work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Updates window ORDER MATTERS, from back to front:
        screen.fill("black")

        player.draw(screen)

        pygame.display.flip() # Updates/draws the finished frame

        # Controls Framerate and recalculates frame delta
        dt = clock.tick(60) / 1000

    """
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    """


if __name__ == "__main__":
    main()