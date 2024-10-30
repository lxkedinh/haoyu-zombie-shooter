import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, dmg, speed, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.dmg = dmg
        self.image = pygame.Surface((50, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.movement()

    def movement(self):
        self.rect.x += self.speed

    def on_hit(self):
        self.despawn()

    def despawn(self):
        self.kill()
