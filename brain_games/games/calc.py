from brain_games import cli


def play():
    print('What is the result of the expression?')
    for _ in range(cli.GAME_ROUNDS):
        num1 = cli.get_rand_val(1, cli.VALUE_INTERVAL)
        num2 = cli.get_rand_val(1, cli.VALUE_INTERVAL)
        set_exp = [f'{num1} + {num2}', f'{num1} - {num2}', f'{num1} * {num2}']
        exp = random.choice(set_exp)
        answer = cli.ask_answer(exp)
        result = eval(exp)
        if cli.check_result(int(answer), result):
            continue
        else:
            return False
    return True
