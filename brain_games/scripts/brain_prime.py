from brain_games.games import prime_game
from brain_games import cli


def main():
    name = cli.welcome_user()
    if prime_game.play_prime():
        cli.congrat_user(name)
    else:
        cli.wrong_bye(name)


if __name__ == '__main__':
    main()
