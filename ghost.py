try:
    import pygame
    from configs import *
    import random
except ImportError:
    print("Please ....fulfil requirements")

GHOST_IMAGE = pygame.image.load(
    'Assets/enemy/round ghost/round ghost idle/sprite_0.png')
GHOST = pygame.transform.scale(
    GHOST_IMAGE, (GHOST_WIDTH, GHOST_HEIGHT))

# --------------------Custom Events----------------------------
PLAYER_HIT = pygame.USEREVENT + 3



class Ghost():
    def __init__(self):
        self.width = GHOST_WIDTH
        self.height = GHOST_HEIGHT
        self.rect = pygame.Rect(WIDTH, random.randint(
            GHOST_HEIGHT, HEIGHT-GHOST_HEIGHT), self.width, self.height)

    def draw(self, WIN):
        WIN.blit(GHOST, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.x -= GHOST_SPEED
        # if player.colliderect(bullet):
        #     pygame.event.post(pygame.event.Event(PLAYER_HIT))
        #     self.bullets.remove(bullet)
