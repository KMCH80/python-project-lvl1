import random
from brain_games import cli


def play():
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    for _ in range(cli.GAME_ROUNDS):
        number = random.randint(1, cli.VALUE_INTERVAL)
        answer = cli.ask_answer(str(number))
        if number % 2:
            result = 'no'
        else:
            result = 'yes'
        if cli.check_result(answer, result):
            continue
        else:
            return False
    return True
