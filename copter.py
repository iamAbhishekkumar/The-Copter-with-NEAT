try:
    import pygame
    from configs import *
except ImportError:
    print("Fulfil requirements")


COPTER_IMAGE = pygame.image.load('Assets/copter/copter1.png')
COPTER = pygame.transform.scale(COPTER_IMAGE, (COPTER_WIDTH, COPTER_HEIGHT))


class Copter():
    def __init__(self):
        self.width = COPTER_WIDTH
        self.height = COPTER_HEIGHT
        self.rect = pygame.Rect(100, HEIGHT // 2, self.width, self.height)

    def draw(self, WIN):
        WIN.blit(COPTER_IMAGE, (self.rect.x, self.rect.y))

    def move_up(self):
        if self.rect.y - COPTER_HEIGHT//2 > 0:
            self.rect.y -= DROP_VEL

    def move_down(self):
        if self.rect.y + COPTER_HEIGHT//2 < HEIGHT:
            self.rect.y += DROP_VEL

    def update(self, keyspressed):
        if keyspressed[pygame.K_SPACE]:
            self.move_up()
        else:
            self.move_down()

    def collision(self):
        pass
