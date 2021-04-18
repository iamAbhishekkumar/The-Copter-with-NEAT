try:
    import pygame
    from configs import *
    import colors
    from events import *
except ImportError:
    print("Fulfil requirements")


COPTER_IMAGE = pygame.image.load('Assets/copter/copter1.png')
width = int(COPTER_IMAGE.get_width() * 1.4)
height = int(COPTER_IMAGE.get_height() * 1.4)
COPTER = pygame.transform.scale(COPTER_IMAGE, (width, height))


class Copter():
    def __init__(self):
        self.hitbox_width = 110
        self.hitbox_height = 54
        self.rect = pygame.Rect(
            100, HEIGHT // 2, self.hitbox_width, self.hitbox_height)

    def draw(self, WIN):
        WIN.blit(COPTER, (self.rect.x - 20, self.rect.y))
        pygame.draw.rect(WIN, colors.RED, (self.rect.x,
                         self.rect.y, self.hitbox_width, self.hitbox_height), 2)

    def move_up(self):
        self.rect.y -= DROP_VEL

    def move_down(self):
        self.rect.y += DROP_VEL

    def update(self, keyspressed):
        if keyspressed[pygame.K_SPACE]:
            self.move_up()
        else:
            self.move_down()

    def collision(self, ghost):
        if self.rect.colliderect(ghost):
            pygame.event.post(pygame.event.Event(PLAYER_HIT))

    def collison_with_boundary(self):
        if self.rect.y < 0 or self.rect.y + self.hitbox_height > HEIGHT:
            pygame.event.post(pygame.event.Event(PLAYER_HIT_BOUNDARY))
