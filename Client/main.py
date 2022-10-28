import config
from Client.screens import screens
from Client.events import events


def main():
    while config.running:
        events()
        screens()


if __name__ == '__main__':
    main()
