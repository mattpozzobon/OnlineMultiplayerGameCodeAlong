import config


def events():
    for event in config.pygame.event.get():
        if event.type == config.pygame.KEYDOWN:
            if event.key == config.pygame.K_ESCAPE:
                config.running = False

