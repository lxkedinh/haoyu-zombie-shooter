import pygame

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


class Zombie(pygame.sprite.Sprite):
    x_pos = 1000
    y_pos = 200

    def __init__(self, speed, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill((79, 163, 93))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)
        self.speed = speed
        self.health = health


player = Player(5)

player_group = pygame.sprite.Group()
player_group.add(player)

zombie = Zombie(3.5, 5)
zombie_group = pygame.sprite.Group()
zombie_group.add(zombie)

bullet = Bullet(10, 5, player.x_pos, player.y_pos)
bullet_group = pygame.sprite.Group()
bullet_group.add(bullet)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    end_time = pygame.time.get_ticks()

    if pygame.mouse.get_pressed()[0] == 1:
        if end_time - start_time >= 100:
            new_bullet = Bullet(10, 5, player.x_pos, player.y_pos)
            bullet_group.add(new_bullet)

    start_time = pygame.time.get_ticks()

    screen.fill((0, 0, 0))
    player_group.draw(screen)
    player_group.update()
    zombie_group.draw(screen)
    zombie_group.update()
    bullet_group.draw(screen)
    bullet_group.update()
    pygame.display.update()
    clock.tick(60)
