try:
    import pygame
except ImportError:
    print("Fulfil requirements")
    
SPAWN_EVENT = pygame.USEREVENT + 1

PLAYER_HIT = pygame.USEREVENT + 2

PLAYER_HIT_BOUNDARY = pygame.USEREVENT + 3