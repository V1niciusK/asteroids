# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    black = pygame.Color(0,0,0)

    # Organizational
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    # Frame rate control
    clock = pygame.time.Clock()
    dt = 0

    # Asteroids
    asteroid_field = AsteroidField()

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
        
        for item in updatable:
            item.update(dt)
        
        for asteroid in asteroids:
            if asteroid.has_collided(player):
                print("Game Over")
                return

        # Updates window ORDER MATTERS, from back to front:
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip() # Updates/draws the finished frame

        # Controls Framerate and recalculates frame delta
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()