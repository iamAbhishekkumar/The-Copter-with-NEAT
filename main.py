try:
    import pygame
    import os
    from configs import *
    import colors
    from ghost import Ghost
    from events import *
    from copter import Copter, COPTER_SPRITE
    import neat
except ImportError:
    print("Please ....fulfil requirements")

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Copter")

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load('Assets/bg.png'), (WIDTH, HEIGHT))


def render_text(text):
    DISPLAY_TEXT = pygame.font.SysFont(
        'comicsans', 35).render(str(text), True, colors.RED)
    padding = 15
    WIN.blit(DISPLAY_TEXT, (WIDTH - DISPLAY_TEXT.get_width() - padding, padding))


BG_movement = 0
COUNTER = 0


def drawBG():
    global BG_movement
    WIN.blit(BACKGROUND_IMAGE, (BG_movement, 0))
    WIN.blit(BACKGROUND_IMAGE, (BG_movement + WIDTH, 0))
    BG_movement -= BACKGROUND_SPEED
    if BG_movement == -WIDTH:
        BG_movement = 0


def draw_window(ghosts, copter, score):
    drawBG()
    render_text(str(score))
    copter.draw(WIN)
    for ghost in ghosts:
        ghost.draw(WIN)
    pygame.display.update()

def score_counter(score):
    global COUNTER
    if COUNTER % 100 == 0:
        COUNTER = 0
        score += 1
    return score

def main():
    clock = pygame.time.Clock()
    run = True
    ghosts = []
    copter = Copter()
    score = 0
    pygame.time.set_timer(SPAWN_EVENT, SPAWN_TIME)
    i = 0
    pressed = {}
    global COUNTER
    while run:
        clock.tick(FPS)
        COUNTER += 1 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == SPAWN_EVENT:
                ghosts.append(Ghost())

        for ghost in ghosts:
            ghost.move()
            if ghost.rect.x < 0 - GHOST_WIDTH:
                ghosts.remove(ghost)
            if copter.collision(ghost):
                ghosts.remove(ghost)
                break

        if copter.collison_with_boundary():
            print("Player hit boundary")

        keys_pressed = pygame.key.get_pressed()
        copter.update(keys_pressed)
        score = score_counter(score)
        draw_window(ghosts, copter, score)



if __name__ == '__main__':
    main()
