import random


def tell_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_task_with_right_answer(value_interval):
    task = random.randint(1, value_interval)
    return [task, get_right_answer(task)]


def get_right_answer(number):
    if is_prime(number):
        return 'yes'
    else:
        return 'no'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(number - 1, 1, -1):
        if number % i:
            continue
        else:
            return False
    return True
