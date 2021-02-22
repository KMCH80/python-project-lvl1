from brain_games.games import prime
from brain_games import cli


def main():
    cli.play(prime.play)


if __name__ == '__main__':
    main()
