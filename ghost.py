try:
    import pygame
    from configs import *
    import random
    import colors
    from events import *
except ImportError:
    print("Please ....fulfil requirements")

GHOST_IMAGE = pygame.image.load(
    'Assets/enemy/round ghost/round ghost idle/sprite_0.png')
GHOST = pygame.transform.scale(
    GHOST_IMAGE, (GHOST_WIDTH, GHOST_HEIGHT))

class Ghost():
    def __init__(self):
        self.hitbox_width = 76
        self.hitbox_height = 70
        self.rect = pygame.Rect(WIDTH, random.randint(
            GHOST_HEIGHT, HEIGHT-GHOST_HEIGHT), self.hitbox_width, self.hitbox_height)

    def draw(self, WIN):
        WIN.blit(GHOST, (self.rect.x - 20, self.rect.y - 30))
        pygame.draw.rect(WIN, colors.GREEN, (self.rect.x,
                    self.rect.y, self.hitbox_width, self.hitbox_height), 2)

    def move(self):
        self.rect.x -= GHOST_SPEED
