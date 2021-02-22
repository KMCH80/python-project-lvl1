from brain_games.games import even
from brain_games import cli


def main():
    cli.play(even.play)


if __name__ == '__main__':
    main()
