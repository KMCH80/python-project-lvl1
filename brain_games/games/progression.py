import random

MIN_LEN = 5
MAX_LEN = 10
MAX_STEP = 10


def tell_rules():
    print('What number is missing in the progression?')


def get_task_with_right_answer(value_interval):
    seq = seq_init(value_interval)
    task_with_right_answer = take_away_elem(seq)
    return [task_with_right_answer[1], task_with_right_answer[0]]


def take_away_elem(seq):
    away_elem = random.choice(seq)
    seq[seq.index(away_elem)] = '..'
    seq_str = ' '.join(seq)
    return [away_elem, seq_str]


def seq_init(value_interval):
    seq_len = random.randint(MIN_LEN, MAX_LEN)
    seq_first_elem = random.randint(1, value_interval)
    step = random.randint(1, MAX_STEP)
    sequence = [str(seq_first_elem)]
    elem = seq_first_elem
    for __ in range(seq_len):
        elem += step
        sequence.append(str(elem))
    return sequence


def get_right_answer(task):
    if is_even(task):
        return 'yes'
    else:
        return 'no'


def is_even(task):
    if task % 2:
        return False
    else:
        return True
