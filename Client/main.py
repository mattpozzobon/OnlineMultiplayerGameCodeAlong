import config
from Client.events import events


def main():
    while config.running:
        events()

        config.pygame.display.update()


if __name__ == '__main__':
    main()
