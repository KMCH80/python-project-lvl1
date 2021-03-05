import random

MIN_VALUE = 1
MAX_VALUE = 100
MIN_LEN = 5
MAX_LEN = 10
MIN_STEP = 1
MAX_STEP = 10
RULES = 'What number is missing in the progression?'


def get_task_with_right_answer():
    progression_len = random.randint(MIN_LEN, MAX_LEN)
    first_elem = random.randint(MIN_VALUE, MAX_VALUE)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression = make_progression(progression_len, first_elem, step)
    index_of_hidden_elem = random.randint(0, len(progression) - 1)
    task = hide_elem_in_progression(progression, index_of_hidden_elem)
    return task, progression[index_of_hidden_elem]


def make_progression(progression_len, first_elem, step):
    progression = [str(first_elem)]
    elem = first_elem
    for __ in range(progression_len):
        elem += step
        progression.append(str(elem))
    return progression


def hide_elem_in_progression(progression, index_of_hidden_elem):
    progression_with_hidden_elem = progression[:]
    progression_with_hidden_elem[index_of_hidden_elem] = '..'
    return ' '.join(progression_with_hidden_elem)
