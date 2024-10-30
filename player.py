import pygame


class Player(pygame.sprite.Sprite):
    x_pos = 400
    y_pos = 200

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3
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
