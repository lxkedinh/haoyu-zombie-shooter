import pygame


class Player(pygame.sprite.Sprite):
    x_pos = 400
    y_pos = 200

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.runSprites = []

        # load all the images for player running animation
        for i in range(8):
            sprite = pygame.image.load(
                f"assets/Character/characterPistolAimingRunning_{i}.png"
            )
            self.runSprites.append(sprite)

        self.runFrameCount = 0
        self.speed = 3
        self.hp = 3
        scaledSprite = pygame.transform.scale(self.runSprites[0], (64 * 1.5, 64 * 1.5))
        self.image = scaledSprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)
        self.facingLeft = False

    def update(self):
        self.movement()

    def movement(self):

        # keep track of frame count for player movement animation loop
        self.runFrameCount = (self.runFrameCount + 1) % 40

        # handle keypress for player movement
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.rect.y -= self.speed
        if keystate[pygame.K_s]:
            self.rect.y += self.speed
        if keystate[pygame.K_a]:
            self.rect.x -= self.speed
            self.facingLeft = True
        if keystate[pygame.K_d]:
            self.rect.x += self.speed
            self.facingLeft = False

        currentSprite = self.runSprites[self.runFrameCount // 5]
        scaledSprite = pygame.transform.scale(currentSprite, (64 * 1.5, 64 * 1.5))

        if self.facingLeft:
            self.image = pygame.transform.flip(scaledSprite, True, False)
        else:
            self.image = scaledSprite

    def on_hit(self, dmg):
        self.hp -= 1
        if self.hp <= 0:
            print("killed")
            self.kill()
