import random

VALUE_INTERVAL = 100
MIN_LEN = 5
MAX_LEN = 10
MAX_STEP = 10
RULES = 'What number is missing in the progression?'


def get_task_with_right_answer():
    seq_len = random.randint(MIN_LEN, MAX_LEN)
    seq_first_elem = random.randint(1, VALUE_INTERVAL)
    step = random.randint(1, MAX_STEP)
    seq = seq_init(seq_len, seq_first_elem, step)
    away_index = random.randint(0, len(seq) - 1)
    task = take_away_elem(seq, away_index)
    return task, seq[away_index]


def take_away_elem(seq, away_index):
    seq_new = seq[:]
    seq_new[away_index] = '..'
    seq_str = ' '.join(seq_new)
    return seq_str


def seq_init(seq_len, seq_first_elem, step):
    sequence = [str(seq_first_elem)]
    elem = seq_first_elem
    for __ in range(seq_len):
        elem += step
        sequence.append(str(elem))
    return sequence
