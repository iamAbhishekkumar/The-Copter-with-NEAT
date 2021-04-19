try:
    import pygame
    import os
    from configs import *
    import colors
    from ghost import Ghost
    from events import *
    from copter import Copter, COPTER_SPRITE
    import neat
    import math
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
GEN = 0


def drawBG():
    global BG_movement
    WIN.blit(BACKGROUND_IMAGE, (BG_movement, 0))
    WIN.blit(BACKGROUND_IMAGE, (BG_movement + WIDTH, 0))
    BG_movement -= BACKGROUND_SPEED
    if BG_movement == -WIDTH:
        BG_movement = 0


def draw_window(ghosts, copters, score):
    drawBG()

    score_text = pygame.font.SysFont(
        'comicsans', 35).render(str(score), True, colors.RED)
    WIN.blit(score_text, (WIDTH - score_text.get_width() - 15, 15))

    gen_text = pygame.font.SysFont(
        'comicsans', 35).render("Gen : "+str(GEN), True, colors.RED)
    WIN.blit(gen_text, (10, 10))

    for copter in copters:
        copter.draw(WIN)
    for ghost in ghosts:
        ghost.draw(WIN)
    pygame.display.update()


def main(genomes, config):
    global GEN
    GEN += 1
    nets = []
    ge = []
    copters = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        copters.append(Copter())
        g.fitness = 0
        ge.append(g)

    clock = pygame.time.Clock()
    run = True
    ghosts = []
    score = 0
    pygame.time.set_timer(SPAWN_EVENT, SPAWN_TIME)
    i = 0
    pressed = {}
    global COUNTER
    while run:
        clock.tick(FPS)
        COUNTER += 1
        if len(copters) == 0:
            run = False
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == SPAWN_EVENT:
                ghosts.append(Ghost())

        for a, ghost in enumerate(ghosts):
            ghost.move()
            if ghost.rect.x < 0 - GHOST_WIDTH:
                ghosts.remove(ghost)
                score += 1
                for g in ge:
                    g.fitness += 5
                continue
            for x, copter in enumerate(copters):
                if copter.collision(ghost):
                    if len(ghosts) != 0:
                        ghosts.pop(a)
                    ge[x].fitness -= 1
                    copters.pop(x)
                    ge.pop(x)
                    nets.pop(x)

                if copter.collison_with_boundary():
                    ge[x].fitness -= 1
                    copters.pop(x)
                    ge.pop(x)
                    nets.pop(x)

                # if COUNTER % 100 == 0:
                #     COUNTER = 0


            for x, copter in enumerate(copters):
                if ghost is not None:
                    output = nets[x].activate((copter.rect.y, abs(
                        copter.rect.x - ghost.rect.x), abs(copter.rect.y - ghost.rect.y)))
                    copter.update(output)

        draw_window(ghosts, copters, score)


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)
    p = neat.Population(config)

    # for what is happening
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50)


if __name__ == '__main__':
    local = os.path.dirname(__file__)
    config_file = os.path.join(local, "config-feedforward.txt")
    run(config_file)
