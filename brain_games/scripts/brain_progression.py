from brain_games.games import progression_game
from brain_games import cli


def main():
    name = cli.welcome_user()
    if progression_game.play_progression():
        cli.congrat_user(name)
    else:
        cli.wrong_bye(name)


if __name__ == '__main__':
    main()
