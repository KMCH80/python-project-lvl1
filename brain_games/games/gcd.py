import random
from brain_games import cli


def play():
    print('Find the greatest common divisor of given numbers.')
    for _ in range(cli.GAME_ROUNDS):
        k = random.randint(2, cli.VALUE_INTERVAL)
        m = random.randint(2, cli.VALUE_INTERVAL)
        number1 = random.randint(2, cli.VALUE_INTERVAL)
        number2 = number1 * k
        number1 = number1 * m
        result = 1
        for i in range(number1, 1, -1):
            if number1 % i or number2 % i:
                continue
            else:
                result = i
                break
        q_set = [str(number1), str(number2)]
        answer = cli.ask_answer(' '.join(q_set))
        if cli.check_result(int(answer), result):
            continue
        else:
            return False
    return True
