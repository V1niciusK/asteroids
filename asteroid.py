import pygame
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = random.random() * 360
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * 100 * dt