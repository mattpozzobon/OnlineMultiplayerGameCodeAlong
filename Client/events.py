import config


def events():
    for event in config.pygame.event.get():
        if event.type == config.pygame.KEYDOWN:
            if event.key == config.pygame.K_ESCAPE:
                config.running = False

            if event.key == config.pygame.K_UP:
                config.angle += 0.2
                print(config.angle)

            if event.key == config.pygame.K_DOWN:
                config.angle -= 0.2
                print(config.angle)


