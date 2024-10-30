import pygame


class Player(pygame.sprite.Sprite):
    x_pos = 400
    y_pos = 200

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3

        self.runSprites = [
            pygame.image.load(f"assets/Character/characterPistolAimingRunning_{i}.png")
            for i in range(8)
        ]

        self.image = self.runSprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

        self.facingLeft = False
        self.facingRight = True
        self.runFrameCount = 0

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
            self.facingLeft = True
            self.facingRight = False
        if keystate[pygame.K_d]:
            self.rect.x += self.speed
            self.facingLeft = False
            self.facingRight = True

        self.runFrameCount = (self.runFrameCount + 1) % 35
        scaledSprite = pygame.transform.scale(
            self.runSprites[self.runFrameCount // 5], (64 * 2, 64 * 2)
        )

        if self.facingLeft:
            self.image = pygame.transform.flip(scaledSprite, True, False)
        else:
            self.image = scaledSprite
