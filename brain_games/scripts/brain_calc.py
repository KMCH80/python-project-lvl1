from brain_games.games import calc_game
from brain_games import cli


def main():
    name = cli.welcome_user()
    if calc_game.play_calc():
        cli.congrat_user(name)
    else:
        cli.wrong_bye(name)


if __name__ == '__main__':
    main()
