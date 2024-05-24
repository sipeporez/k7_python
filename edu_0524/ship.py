import pygame

from setting import Setting


class Ship:
    def __init__(self, screen_surf):
        self.IMG_PATH = "images/ship.bmp"
        self.SPEED = 10

        self.ship_img_surf = pygame.image.load(self.IMG_PATH).convert()
        self.ship_rect = self.ship_img_surf.get_rect()
        self.screen_surf = screen_surf

    def render(self):
        self.screen_surf.blit(self.ship_img_surf, self.ship_rect)

    def default_pos(self):
        self.ship_rect.midbottom = self.screen_surf.get_rect().midbottom

    def move_left(self):
        if 0 < self.ship_rect.x:
            self.ship_rect.x = self.ship_rect.x - self.SPEED

    def move_right(self):
        screen_rect = self.screen_surf.get_rect()
        if self.ship_rect.x < screen_rect.width - self.ship_rect.width:
            self.ship_rect.x = self.ship_rect.x + self.SPEED

    def update(self):
        pass
        # if  self.left_pressed:
        #     self.ship.move_left()
        # if self.right_pressed:
        #     self.ship.move_right()

    def get_rect(self):
        return self.ship_rect
