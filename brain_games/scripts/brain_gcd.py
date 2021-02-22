from brain_games.games import gcd
from brain_games import cli


def main():
    cli.play(gcd.play)


if __name__ == '__main__':
    main()
