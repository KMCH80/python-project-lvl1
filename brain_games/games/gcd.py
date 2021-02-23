from brain_games import cli


def play():
    print('Find the greatest common divisor of given numbers.')
    for _ in range(cli.GAME_ROUNDS):
        result = 1
        while result == 1:
            number1 = cli.get_rand_val(2, cli.VALUE_INTERVAL)
            number2 = cli.get_rand_val(2, cli.VALUE_INTERVAL)
            result = get_div(number1, number2)
        q_set = [str(number1), str(number2)]
        answer = cli.ask_answer(' '.join(q_set))
        if cli.check_result(int(answer), result):
            continue
        else:
            return False
    return True


def get_div(number1, number2):
    for i in range(min(number1,number2), 0, -1):
        if number1 % i or number2 % i:
            continue
        else:
            return i