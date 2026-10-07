import pygame

from bullet import Bullet
from settings import MAX_HP, TANK_SIZE, TANK_SPEED


class Tank:
    def __init__(self, x, y, color, controls, name):
        self.rect = pygame.Rect(x, y, TANK_SIZE, TANK_SIZE)
        self.color = color
        self.controls = controls
        self.name = name
        self.hp = MAX_HP
        self.direction = pygame.Vector2(1, 0)
        self.cooldown = 0

    def update(self, keys, bounds):
        move = pygame.Vector2(0, 0)

        if keys[self.controls["up"]]:
            move.y -= 1
            self.direction = pygame.Vector2(0, -1)
        if keys[self.controls["down"]]:
            move.y += 1
            self.direction = pygame.Vector2(0, 1)
        if keys[self.controls["left"]]:
            move.x -= 1
            self.direction = pygame.Vector2(-1, 0)
        if keys[self.controls["right"]]:
            move.x += 1
            self.direction = pygame.Vector2(1, 0)

        if move.length_squared() > 0:
            move = move.normalize() * TANK_SPEED
            self.rect.x += int(move.x)
            self.rect.y += int(move.y)
            self.rect.clamp_ip(bounds)

        if self.cooldown > 0:
            self.cooldown -= 1

    def shoot(self):
        if self.cooldown > 0 or self.hp <= 0:
            return None

        self.cooldown = 25
        muzzle = pygame.Vector2(self.rect.center) + self.direction * 30
        return Bullet(muzzle.x, muzzle.y, self.direction, self)

    def hit(self, damage):
        self.hp = max(0, self.hp - damage)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=7)
        center = pygame.Vector2(self.rect.center)
        end = center + self.direction * 32
        pygame.draw.line(screen, (25, 25, 25), center, end, 7)
        pygame.draw.circle(screen, (25, 25, 25), self.rect.center, 8)
