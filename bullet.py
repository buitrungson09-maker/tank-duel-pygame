import pygame

from settings import BULLET_SPEED, YELLOW


class Bullet:
    def __init__(self, x, y, direction, owner):
        self.rect = pygame.Rect(x - 5, y - 5, 10, 10)
        self.direction = pygame.Vector2(direction)
        self.owner = owner
        self.active = True

    def update(self, width, height):
        self.rect.x += int(self.direction.x * BULLET_SPEED)
        self.rect.y += int(self.direction.y * BULLET_SPEED)

        if not pygame.Rect(0, 0, width, height).colliderect(self.rect):
            self.active = False

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, self.rect.center, 5)
