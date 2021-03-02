import random

VALUE_INTERVAL = 1000
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task_with_right_answer():
    task = random.randint(1, VALUE_INTERVAL)
    return task, get_right_answer(task)


def get_right_answer(number):
    if is_prime(number):
        return 'yes'
    else:
        return 'no'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(number - 1, 1, -1):
        if number % i == 0:
            return False
    return True
