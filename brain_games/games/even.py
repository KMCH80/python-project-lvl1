import random

VALUE_INTERVAL = 1000
RULES = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def get_task_with_right_answer():
    task = random.randint(1, VALUE_INTERVAL)
    return task, get_right_answer(task)


def get_right_answer(task):
    if is_even(task):
        return 'yes'
    else:
        return 'no'


def is_even(task):
    return task % 2 == 0
