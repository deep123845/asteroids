from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        log_event("asteroid_split")
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(ASTEROID_SPLIT_MIN_ANGLE, ASTEROID_SPLIT_MAX_ANGLE)
        velocity_l = self.velocity.rotate(angle * -1)
        velocity_r = self.velocity.rotate(angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_l = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_r = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_l.velocity = velocity_l * 1.2
        asteroid_r.velocity = velocity_r * 1.2
