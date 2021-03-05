import random

MIN_VALUE = 2
MAX_VALUE = 100
RULES = 'Find the greatest common divisor of given numbers.'


def get_task_with_right_answer():
    number1 = random.randint(MIN_VALUE, MAX_VALUE)
    number2 = random.randint(MIN_VALUE, MAX_VALUE)
    right_answer = get_gcd(number1, number2)
    task = f'{number1} {number2}'
    return task, str(right_answer)


def get_gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 + number2
