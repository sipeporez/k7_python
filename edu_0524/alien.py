import pygame


class Alien:
    def __init__(self, screen_surf):
        self.IMG_PATH = "images/alien.bmp"

        self.alien_img_surf = pygame.image.load(self.IMG_PATH).convert()
        self.alien_rect = self.alien_img_surf.get_rect()
        self.screen_surf = screen_surf

    def render(self):
        self.screen_surf.blit(
            self.alien_img_surf,
            self.alien_rect)
    
    def move_pos(self, x, y):
        self.alien_rect.x = x
        self.alien_rect.y = y
         
        # self.alien_rect.midtop = self.screen_surf.get_rect().midtop
        