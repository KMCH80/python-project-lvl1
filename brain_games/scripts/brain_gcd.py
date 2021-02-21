from brain_games.games import gcd_game
from brain_games import cli


def main():
    name = cli.welcome_user()
    if gcd_game.play_gcd():
        cli.congrat_user(name)
    else:
        cli.wrong_bye(name)


if __name__ == '__main__':
    main()
