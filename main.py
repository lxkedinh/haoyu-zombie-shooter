import pygame
from bullet import Bullet
from player import Player
from zombie import Zombie
import utils

pygame.init()
clock = pygame.time.Clock()
screen_height = 768
screen = pygame.display.set_mode((utils.screen_width, utils.screen_height))


zombie_group = pygame.sprite.Group()


player = Player()

player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

clicked = False
last_click_time = None
player_shoot_cd = 100

last_spawn_time = 0
zombie_spawn_cd = 1000


def spawn_zombie():
    zombie = Zombie(player)
    zombie_group.add(zombie)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    current_time = pygame.time.get_ticks()

    # spawn zombie
    if current_time - last_spawn_time >= zombie_spawn_cd:
        spawn_zombie()
        last_spawn_time = pygame.time.get_ticks()

    keystate = pygame.key.get_pressed()
    if (keystate[pygame.K_SPACE] or pygame.mouse.get_pressed()[0] == 1) and not clicked:
        clicked = True
        last_click_time = pygame.time.get_ticks()
        new_bullet = Bullet(10, 20, player.rect.centerx, player.rect.centery)
        bullet_group.add(new_bullet)

    if last_click_time and current_time - last_click_time >= player_shoot_cd:
        clicked = False

    # Check for collision between bullet and zombie
    for bullet in bullet_group.sprites():
        hit_zombies = pygame.sprite.spritecollide(bullet, zombie_group, dokill=False)
        for zombie in hit_zombies:
            zombie.get_hit(bullet.dmg)
            bullet.on_hit()
        pass

    screen.fill((0, 0, 0))
    player_group.draw(screen)
    player_group.update()
    zombie_group.draw(screen)
    zombie_group.update()
    bullet_group.draw(screen)
    bullet_group.update()
    pygame.display.update()
    clock.tick(60)
