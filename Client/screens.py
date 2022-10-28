import config
from Client.Components.fpstab import FpsTab

fps = FpsTab(config.window, 100, 100, 100, 100)

def screens():
    config.clock.tick(config.fps)

    config.screen.blit(config.topbar, (1, 1))
    config.screen.blit(config.window, (1, 40))

    fps.render(config.clock.get_fps())

    config.pygame.display.update()