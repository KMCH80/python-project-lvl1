from brain_games.games import calc
from brain_games import cli


def main():
    cli.play(calc.play)


if __name__ == '__main__':
    main()
