import random

MIN_VALUE = 1
MAX_VALUE = 1000
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task_with_right_answer():
    task = random.randint(MIN_VALUE, MAX_VALUE)
    return task, get_right_answer(task)


def get_right_answer(task):
    if is_even(task):
        return 'yes'
    else:
        return 'no'


def is_even(task):
    return task % 2 == 0
