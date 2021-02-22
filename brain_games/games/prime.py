import random
from brain_games import cli


def play():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(cli.GAME_ROUNDS):
        number = random.randint(2, cli.VALUE_INTERVAL)
        result = 'yes'
        for i in range(number - 1, 1, -1):
            if number % i:
                continue
            else:
                result = 'no'
                break
        answer = cli.ask_answer(str(number))
        if cli.check_result(answer, result):
            continue
        else:
            return False
    return True
