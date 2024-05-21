# 원본 코드 출처 : https://www.pygame.org/docs/tut/newbieguide.html
# pip install pygame
import pygame


def init():
    pygame.init()
    screen_surf = pygame.display.set_mode((1280, 720))
    return screen_surf

# 이미지 로드
def create_ship(screen_surf):
    ship_img = pygame.image.load("image/ship.bmp")
    ship_rect = ship_img.get_rect()
    ship_rect.midbottom = screen_surf.get_rect().midbottom
    return ship_img, ship_rect


def create_aliens():
    alien_img = pygame.image.load("image/alien.bmp")
    alien_rect = alien_img.get_rect()
    aliens = []
    for i in range(5):
        alien = pygame.rect.Rect(200 * i, 100, 100, 100)
        aliens.append(alien)

    return alien_img, aliens


screen_surf = init()


def render_object(screen_surf, ship_img, ship_rect, alien_img, aliens, bullets):
    screen_surf.blit(ship_img, ship_rect)
    for alien in aliens:
        screen_surf.blit(alien_img, alien)
    if bullets:
        for bullet in bullets:
            pygame.draw.rect(screen_surf, "red", bullet)
            if bullet.y < 0:
                bullets.remove(bullet)
    # 외계인과 총알 충돌시 외계인 삭제
    for alien in aliens:
        for bullet in bullets:
            if pygame.rect.Rect.colliderect(bullet, alien):
                aliens.remove(alien)
                bullets.remove(bullet)

    if len(aliens) == 0:
        print("Game Over!")
        is_running = False


ship_img, ship_rect = create_ship(screen_surf)
alien_img, aliens = create_aliens()

alien_x_direction = 1  # False: -1, 1: right
alien_x_direction_changed = False
# 총알 설정
bullet_rect = None
bullets = []

clock = pygame.time.Clock()

# 키 입력 받는 변수
press_left = False
press_right = False
press_up = False
press_down = False
press_space = False


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        # 키가 눌린 상태일때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                press_left = True
            if event.key == pygame.K_RIGHT:
                press_right = True
            if event.key == pygame.K_UP:
                press_up = True
            if event.key == pygame.K_DOWN:
                press_down = True
            if event.key == pygame.K_SPACE:
                press_space = True
                if len(bullets) < 5:
                    bullet_rect = pygame.rect.Rect(0, 0, 6, 30)
                    bullet_rect.midbottom = ship_rect.midtop
                    bullets.append(bullet_rect)

        # 키가 눌리지 않은 상태일때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                press_left = False
            if event.key == pygame.K_RIGHT:
                press_right = False
            if event.key == pygame.K_UP:
                press_up = False
            if event.key == pygame.K_DOWN:
                press_down = False
            if event.key == pygame.K_SPACE:
                press_space = False

    # Do logical updates here.
    # ...
    if press_right:
        if screen_surf.get_width() - ship_rect.width > ship_rect.x:
            ship_rect.x += 4
    if press_left:
        if 0 < ship_rect.x:
            ship_rect.x -= 4
    if press_up:
        ship_rect.y -= 4
    if press_down:
        if screen_surf.get_height() - ship_rect.height > ship_rect.y:
            ship_rect.y += 4
    if bullets:
        for bullet in bullets:
            bullet.y -= 12
    if aliens:
        screen_rect = screen_surf.get_rect()
        for alien in aliens:
            if screen_rect.width - alien.width < alien.x:
                alien_x_direction = -1
                alien_x_direction_changed = True
                break
            elif alien.x < screen_rect.x:
                alien_x_direction = 1
                alien_x_direction_changed = True
                break
        for alien in aliens:
            print(alien.y, alien.x)
            alien.x += alien_x_direction * 2
            if alien_x_direction_changed:
                alien.y += alien_img.get_rect().height
        alien_x_direction_changed = False

    screen_surf.fill("#303030")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    render_object(screen_surf, ship_img, ship_rect, alien_img, aliens, bullets)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)
