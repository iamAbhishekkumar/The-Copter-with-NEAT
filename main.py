
try:
    import pygame
    import os
    from configs import *
    from player import *
except ImportError:
    print("Please ....fulfil requirements")

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Copter")


def render_text(text):
    DISPLAY_TEXT = pygame.font.SysFont(
        'comicsans', 35).render(str(text), True, colors.RED)
    padding = 15
    WIN.blit(DISPLAY_TEXT, (WIDTH - DISPLAY_TEXT.get_width() - padding, padding))


BG_movement = 0


# def drawBG():
#     global BG_movement
#     WIN.blit(BACKGROUND_IMAGE, (BG_movement, 0))
#     WIN.blit(BACKGROUND_IMAGE, (BG_movement + WIDTH, 0))
#     BG_movement -= BACKGROUND_SPEED
#     if BG_movement == -WIDTH:
#         BG_movement = 0


def draw_window(player, enemy, score):
    
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        
if __name__ == '__main__':
    main()