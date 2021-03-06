import random

MIN_VALUE = 1
MAX_VALUE = 100
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task_with_right_answer():
    task = random.randint(MIN_VALUE, MAX_VALUE)
    return task, get_right_answer(task)


def get_right_answer(number):
    if is_prime(number):
        return 'yes'
    else:
        return 'no'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True
