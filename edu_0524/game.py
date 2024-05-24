import sys
import pygame

from bullet import Bullet
from ship import Ship
from alien import Alien


class Game:
    def __init__(self, title):
        self.title = title

        pygame.init()

        self._create_screen()
        self._create_ship()
        self._create_alien()
        self._create_score()

        self.bullets = []

        self.clock = pygame.time.Clock()

    def start(self):
        while True:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        self.left_pressed = True
                    if e.key == pygame.K_RIGHT:
                        self.right_pressed = True

                    if e.key == pygame.K_SPACE:
                        bullet = Bullet(self.screen_surf)
                        bullet.move_bullet_pos(self.ship.get_rect())
                        self.bullets.append(bullet)

                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT:
                        self.left_pressed = False 
                    if e.key == pygame.K_RIGHT:
                        self.right_pressed = False
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()

            # self.ship.update()

            self._render()

            pygame.display.flip()

            self.clock.tick(60)

    def _render(self):
        self.screen_surf.fill("#404040")

        for alien in self.aliens:
            alien.render()

        for bullet in self.bullets:
            bullet.render()


        self.ship.render()

        self.screen_surf.blit(
                self.score_font,
                (
                    100,
                    100,
                    self.score_font.get_rect().width,
                    self.score_font.get_rect().height,
                ),
            )

    def _create_alien(self):
        self.aliens = []
        self.alien = Alien(self.screen_surf)
        for i in range(1, 4):
            for j in range(10):
                self.alien = Alien(self.screen_surf)
                x_pos = 50 + self.alien.alien_rect.width*2 * j
                y_pos = self.alien.alien_rect.height*2 * i
                self.alien.move_pos(x_pos, y_pos)
                self.aliens.append(self.alien)

    def _create_score(self):
        self.score_font = pygame.font.SysFont(None, 64).render(str(5678), True, "black")

    def _create_ship(self):
        self.ship = Ship(self.screen_surf)
        self.ship.default_pos()

    def _create_screen(self):
        self.screen_surf = pygame.display.set_mode((1280, 720))



    def __str__(self):
        return self.title


game = Game("Space Invader")
game.start()
