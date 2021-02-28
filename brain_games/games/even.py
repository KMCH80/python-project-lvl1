import random


def tell_rules():
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')


def get_task_with_right_answer(value_interval):
    task = random.randint(1, value_interval)
    return [task, get_right_answer(task)]


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
