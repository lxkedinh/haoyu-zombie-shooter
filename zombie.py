import pygame
import random
import math
import utils


class Zombie(pygame.sprite.Sprite):

    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.walkSprites = []
        for i in range(5):
            self.walkSprites.append(
                pygame.image.load(f"assets/Zombie/Walk/zombie_Walk_{i}.png")
            )
        self.walkFrameCount = 0
        self.facingLeft = False

        self.speed = 1
        self.health = 50
        self.target = target

        # spawn in random position
        self.x_pos = utils.screen_width * random.randint(0, 1)
        self.y_pos = utils.screen_height * random.randint(0, 1)

        self.image = self.walkSprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

    def update(self):
        self.movement()

    def movement(self):
        player = self.target
        distance = math.sqrt(
            (player.rect.centerx - self.rect.centerx) ** 2
            + (player.rect.centery - self.rect.centery) ** 2
        )

        self.walkFrameCount = (self.walkFrameCount + 1) % 20

        if distance > 0:  # Prevent division by zero
            direction_x = (player.rect.centerx - self.rect.centerx) / distance
            direction_y = (player.rect.centery - self.rect.centery) / distance
            self.facingLeft = direction_x < 0

            currentSprite = self.walkSprites[self.walkFrameCount // 4]
            scaledSprite = pygame.transform.scale(currentSprite, (64 * 2, 64 * 2))
            if self.facingLeft:
                self.image = pygame.transform.flip(scaledSprite, True, False)
            else:
                self.image = scaledSprite

            self.rect.x += direction_x * self.speed
            self.rect.y += direction_y * self.speed

    def get_hit(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.despawn()

    def despawn(self):
        self.kill()
