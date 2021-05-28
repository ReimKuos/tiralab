from ui.commandlineui import CommandlineUI


def main():
    """
    At the moment function just meant to generate music midi from the data,
    most will moved somewhere else in the end
    """
    user_interface = CommandlineUI()
    user_interface.start()


if __name__ == "__main__":
    main()
