import pygame

from settings import (
    BG_COLOR, BULLET_DAMAGE, FPS, GREEN, HEIGHT, MAX_HP, RED, WHITE, WIDTH
)
from tank import Tank


def draw_hud(screen, font, tank1, tank2):
    p1 = font.render(f"{tank1.name}: {tank1.hp}/{MAX_HP} HP", True, WHITE)
    p2 = font.render(f"{tank2.name}: {tank2.hp}/{MAX_HP} HP", True, WHITE)
    screen.blit(p1, (20, 15))
    screen.blit(p2, (WIDTH - p2.get_width() - 20, 15))


def draw_center_text(screen, font, text):
    surface = font.render(text, True, WHITE)
    rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(surface, rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tank Duel 2D")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 32)
    big_font = pygame.font.Font(None, 64)

    p1_controls = {
        "up": pygame.K_w, "down": pygame.K_s,
        "left": pygame.K_a, "right": pygame.K_d,
        "shoot": pygame.K_SPACE,
    }
    p2_controls = {
        "up": pygame.K_UP, "down": pygame.K_DOWN,
        "left": pygame.K_LEFT, "right": pygame.K_RIGHT,
        "shoot": pygame.K_RETURN,
    }

    tank1 = Tank(100, HEIGHT // 2, GREEN, p1_controls, "Player 1")
    tank2 = Tank(WIDTH - 150, HEIGHT // 2, RED, p2_controls, "Player 2")
    tank2.direction = pygame.Vector2(-1, 0)

    bullets = []
    arena = pygame.Rect(10, 55, WIDTH - 20, HEIGHT - 65)
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == tank1.controls["shoot"]:
                    bullet = tank1.shoot()
                    if bullet:
                        bullets.append(bullet)
                if event.key == tank2.controls["shoot"]:
                    bullet = tank2.shoot()
                    if bullet:
                        bullets.append(bullet)

        keys = pygame.key.get_pressed()

        if tank1.hp > 0 and tank2.hp > 0:
            tank1.update(keys, arena)
            tank2.update(keys, arena)

            for bullet in bullets:
                bullet.update(WIDTH, HEIGHT)
                target = tank2 if bullet.owner is tank1 else tank1
                if bullet.active and target.hp > 0 and bullet.rect.colliderect(target.rect):
                    target.hit(BULLET_DAMAGE)
                    bullet.active = False

            bullets = [bullet for bullet in bullets if bullet.active]

        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, (80, 90, 75), arena, 3)

        tank1.draw(screen)
        tank2.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)

        draw_hud(screen, font, tank1, tank2)

        if tank1.hp <= 0:
            draw_center_text(screen, big_font, "PLAYER 2 WINS!")
        elif tank2.hp <= 0:
            draw_center_text(screen, big_font, "PLAYER 1 WINS!")

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
