import pygame
import random
import math
import utils


class Zombie(pygame.sprite.Sprite):

    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)

        self.walkSprites = [
            pygame.image.load(f"assets/Zombie/Walk/zombie_Walk_{i}.png")
            for i in range(4)
        ]
        self.walkFrameCount = 0
        self.image = self.walkSprites[0]
        self.rect = self.image.get_rect()
        self.rect.height = 64
        self.rect.width = 64
        self.facingLeft = False
        self.facingRight = True

        self.speed = 1
        self.health = 50
        self.target = target

        # spawn in random position
        self.x_pos = utils.screen_width * random.randint(0, 1)
        self.y_pos = utils.screen_height * random.randint(0, 1)

        self.rect.center = (self.x_pos, self.y_pos)

    def update(self):
        self.movement()

    def movement(self):
        player = self.target
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y
        distance = math.hypot(dx, dy)
        dx = dx / distance
        dy = dy / distance

        # calculate direction to face
        self.facingLeft = True if dx < 0 else False
        self.facingRight = not self.facingLeft

        self.walkFrameCount = (self.walkFrameCount + 1) % 20
        scaledSprite = pygame.transform.scale(
            self.walkSprites[self.walkFrameCount // 5], (64 * 2, 64 * 2)
        )

        if self.facingLeft:
            self.image = pygame.transform.flip(scaledSprite, True, False)
        else:
            self.image = scaledSprite

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def get_hit(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.despawn()

    def despawn(self):
        self.kill()
