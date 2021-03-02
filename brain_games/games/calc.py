import random
import sys

VALUE_INTERVAL_PLUS_MINUS = 1000
VALUE_INTERVAL_MULT = 10
RULES = 'What is the result of the expression?'


def get_task_with_right_answer():
    signs_set = ['+', '-', '*']
    str_sign = random.choice(signs_set)
    if str_sign == '*':
        val_int = VALUE_INTERVAL_MULT
    else:
        val_int = VALUE_INTERVAL_PLUS_MINUS
    num1 = random.randint(1, val_int)
    num2 = random.randint(1, val_int)
    task = f'{num1} {str_sign} {num2}'
    return task, get_right_answer(num1, num2, str_sign)


def get_right_answer(num1, num2, str_sign):
    if str_sign == '+':
        return str(num1 + num2)
    elif str_sign == '-':
        return str(num1 - num2)
    elif str_sign == '*':
        return str(num1 * num2)
    else:
        sys.exit('Error. Wrong sign in string of signs.')
