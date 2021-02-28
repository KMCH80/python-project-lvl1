import random


def tell_rules():
    print('What is the result of the expression?')


def get_task_with_right_answer(value_interval):
    num1 = random.randint(1, value_interval)
    num2 = random.randint(1, value_interval)
    signs_set = ['+', '-', '*']
    str_sign = random.choice(signs_set)
    task = f'{num1} {str_sign} {num2}'
    return [task, get_right_answer(num1, num2, str_sign)]


def get_right_answer(num1, num2, str_sign):
    if str_sign == '+':
        return str(num1 + num2)
    elif str_sign == '-':
        return str(num1 - num2)
    elif str_sign == '*':
        return str(num1 * num2)
