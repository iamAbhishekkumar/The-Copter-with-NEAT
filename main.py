try:
    import pygame
    import os
    from configs import *
    import colors
    from ghost import Ghost
    from events import *
    from copter import Copter,COPTER_SPRITE
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


def drawBG():
    global BG_movement
    WIN.blit(BACKGROUND_IMAGE, (BG_movement, 0))
    WIN.blit(BACKGROUND_IMAGE, (BG_movement + WIDTH, 0))
    BG_movement -= BACKGROUND_SPEED
    if BG_movement == -WIDTH:
        BG_movement = 0



def draw_window(ghosts, copter):  
    drawBG()
    copter.draw(WIN)
    for ghost in ghosts:
        ghost.draw(WIN)
    pygame.display.update()


def main():          
    clock = pygame.time.Clock()
    run = True
    ghosts = []
    copter = Copter()
    pygame.time.set_timer(SPAWN_EVENT, SPAWN_TIME)
    i = 0
    pressed = {}
    while run:  
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == SPAWN_EVENT:
                ghosts.append(Ghost())                
            
        for ghost in ghosts:
            ghost.move()
            copter.collision(ghost)
            if ghost.rect.x < 0 - GHOST_WIDTH:
                ghosts.remove(ghost)
            if event.type == PLAYER_HIT:
                ghosts.remove(ghost)
                
        if event.type == PLAYER_HIT_BOUNDARY:
            print("Player hit boundary")
            

        keys_pressed = pygame.key.get_pressed()

        copter.update(keys_pressed)
        copter.collison_with_boundary()
        
        draw_window(ghosts, copter)


if __name__ == '__main__':
    main()
