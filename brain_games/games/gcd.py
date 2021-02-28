import random


def tell_rules():
    print('Find the greatest common divisor of given numbers.')


def get_task_with_right_answer(value_interval):
    two_numbers = generate_two_numbers(value_interval)
    result = get_right_answer(two_numbers[0], two_numbers[1])
    q_set = f'{two_numbers[0]} {two_numbers[1]}'
    return [q_set, str(result)]


def generate_two_numbers(value_interval):
    number1 = number2 = 1
    while get_right_answer(number1, number2) == 1:
        number1 = random.randint(2, value_interval)
        number2 = random.randint(2, value_interval)
    return [number1, number2]


def get_right_answer(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 + number2
