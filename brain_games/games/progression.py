from brain_games import cli

MAX_LEN = 10
MIN_LEN = 5
MAX_STEP = 10

def play():
    print('What number is missing in the progression?')
    for _ in range(cli.GAME_ROUNDS):
        seq_len = cli.get_rand_val(MIN_LEN, MAX_LEN)
        seq_first_elem = cli.get_rand_val(1, cli.VALUE_INTERVAL)
        step = cli.get_rand_val(1, MAX_STEP)
        sequence = [str(seq_first_elem)]
        elem = seq_first_elem
        for __ in range(seq_len):
            elem += step
            sequence.append(str(elem))
        take_away_elem = cli.get_rand_val(1, seq_len)
        result = sequence[take_away_elem - 1]
        sequence[take_away_elem - 1] = '..'
        seq_string = ' '.join(sequence)
        answer = cli.ask_answer(seq_string)
        if cli.check_result(answer, result):
            continue
        else:
            return False
    return True
