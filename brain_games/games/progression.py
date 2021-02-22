import random
from brain_games import cli


def play():
    MAX_LEN = 10
    MIN_LEN = 5
    MAX_STEP = 10
    print('What number is missing in the progression?')
    for _ in range(cli.GAME_ROUNDS):
        seq_len = random.randint(MIN_LEN, MAX_LEN)
        seq_first_elem = random.randint(1, cli.VALUE_INTERVAL)
        step = random.randint(1, MAX_STEP)
        sequence = [str(seq_first_elem)]
        elem = seq_first_elem
        for i in range(seq_len):
            elem += step
            sequence.append(str(elem))
        take_away_elem = random.randint(1, seq_len)
        result = sequence[take_away_elem - 1]
        sequence[take_away_elem - 1] = '..'
        seq_string = ', '.join(sequence)
        answer = cli.ask_answer(seq_string)
        if cli.check_result(answer, result):
            continue
        else:
            return False
    return True
