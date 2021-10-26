import pygame

C_BACKGROUND = (0, 0, 0)
C_TEXT = (0, 255, 0)


def render_lines(font, lines):
    pics = []
    for line in lines:
        pics.append(font.render(line, True, C_TEXT))
    return pics


def draw(screen, lines, y):
    for line in lines:
        screen.blit(line, (0, y))
        y += 20


def main(lines):
    pygame.init()

    size = (700, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("scrolling message")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    text = render_lines(font, lines)

    recty = 580
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(C_BACKGROUND)
        draw(screen, text, recty)
        recty -= 1

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main([
    "T'was the night before maintenance",
    "when all through the data centre,",
])
