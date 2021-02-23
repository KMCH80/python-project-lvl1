from brain_games import cli


def play():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(cli.GAME_ROUNDS):
        number = cli.get_rand_val(2, cli.VALUE_INTERVAL)
        if is_prime(number):
            result = 'yes'
        else:
            result = 'no'
        answer = cli.ask_answer(str(number))
        if cli.check_result(answer, result):
            continue
        else:
            return False
    return True


def is_prime(number):
    for i in range(number - 1, 1, -1):
        if number % i:
            continue
        else:
            return False
    return True
