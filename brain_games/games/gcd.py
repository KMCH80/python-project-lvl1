from brain_games import cli


def play():
    print('Find the greatest common divisor of given numbers.')
    for _ in range(cli.GAME_ROUNDS):
        k = cli.get_rand_val(2, cli.VALUE_INTERVAL)
        number2 = k * cli.get_rand_val(2, cli.VALUE_INTERVAL)
        number1 = k * cli.get_rand_val(2, cli.VALUE_INTERVAL)
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
