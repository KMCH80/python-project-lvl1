from brain_games.games import even_game
from brain_games import cli


def main():
    name = cli.welcome_user()
    if even_game.play_even():
        cli.congrat_user(name)
    else:
        cli.wrong_bye(name)


if __name__ == '__main__':
    main()
