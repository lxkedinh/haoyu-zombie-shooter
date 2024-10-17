import pygame
import math

pygame.init()
clock = pygame.time.Clock()
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))


class Player(pygame.sprite.Sprite):
    x_pos = 400
    y_pos = 200

    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

    def update(self):
        self.movement()

    def movement(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_w]:
            self.rect.y -= self.speed
        if keystate[pygame.K_s]:
            self.rect.y += self.speed
        if keystate[pygame.K_a]:
            self.rect.x -= self.speed
        if keystate[pygame.K_d]:
            self.rect.x += self.speed


class Bullet(pygame.sprite.Sprite):

    def __init__(self, dmg, speed, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.dmg = dmg
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.movement()

    def movement(self):
        self.rect.x += self.speed

    def check_hit(self, zombie):
        if pygame.sprite.collide_rect(self, zombie):
            self.despawn()

    def despawn(self):
        self.kill()


class Zombie(pygame.sprite.Sprite):
    x_pos = 1000
    y_pos = 200

    def __init__(self, speed, health, target):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill((79, 163, 93))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)
        self.speed = speed
        self.health = health
        self.target = target

    def update(self):
        self.movement()

    def movement(self):
        player = self.target
        distance = math.sqrt(
            (player.rect.centerx - self.rect.centerx) ** 2
            + (player.rect.centery - self.rect.centery) ** 2
        )

        if distance > 0:  # Prevent division by zero
            direction_x = (player.rect.centerx - self.rect.centerx) / distance
            direction_y = (player.rect.centery - self.rect.centery) / distance

            self.rect.x += direction_x * self.speed
            self.rect.y += direction_y * self.speed


player = Player(5)

player_group = pygame.sprite.Group()
player_group.add(player)

zombie = Zombie(3.5, 5, player)
zombie_group = pygame.sprite.Group()
zombie_group.add(zombie)

bullet_group = pygame.sprite.Group()

clicked = False
last_click_time = None
player_shoot_cd = 100

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keystate = pygame.key.get_pressed()
    if (keystate[pygame.K_SPACE] or pygame.mouse.get_pressed()[0] == 1) and not clicked:
        clicked = True
        last_click_time = pygame.time.get_ticks()
        new_bullet = Bullet(10, 5, player.rect.centerx, player.rect.centery)

    current_time = pygame.time.get_ticks()
    if last_click_time and current_time - last_click_time >= player_shoot_cd:
        clicked = False

    # Check for collision between bullet and zombie
    for bullet in bullet_group.sprites():
        bullet.check_hit(zombie)

    screen.fill((0, 0, 0))
    player_group.draw(screen)
    player_group.update()
    zombie_group.draw(screen)
    zombie_group.update()
    bullet_group.draw(screen)
    bullet_group.update()
    pygame.display.update()
    clock.tick(60)
