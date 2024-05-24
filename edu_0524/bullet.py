import pygame


class Bullet:
    def __init__(self, screen_surf):
        self.bullet_rect = pygame.rect.Rect(0, 0, 5, 10)
        self.screen_surf = screen_surf

    def render(self):
        pygame.draw.rect(self.screen_surf, "red", self.bullet_rect)

    def move_bullet_pos(self, ship_rect):
        self.bullet_rect.midbottom = ship_rect.midtop


# bullet = Bullet()
# bullet.move_bullet_pos(ship_rect)
# bullet.render()
