from brain_games import cli


def play():
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    for _ in range(cli.GAME_ROUNDS):
        number = cli.get_rand_val(1, cli.VALUE_INTERVAL)
        answer = cli.ask_answer(str(number))
        result = is_even(number)
        if cli.check_result(answer, result):
            continue
        else:
            return False
    return True


def is_even(number):
    if number % 2:
        return 'no'
    else:
        return 'yes'
        