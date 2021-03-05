import random

MIN_VALUE = 1
MAX_VALUE = 100
RULES = 'What is the result of the expression?'


def get_task_with_right_answer():
    signs = ['+', '-', '*']
    sign = random.choice(signs)
    num1 = random.randint(MIN_VALUE, MAX_VALUE)
    num2 = random.randint(MIN_VALUE, MAX_VALUE)
    task = f'{num1} {sign} {num2}'
    return task, get_right_answer(num1, num2, sign)


def get_right_answer(num1, num2, sign):
    if sign == '+':
        return str(num1 + num2)
    elif sign == '-':
        return str(num1 - num2)
    elif sign == '*':
        return str(num1 * num2)
    else:
        raise Exception('Error in signs')
