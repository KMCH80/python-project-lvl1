import random
import prompt

GAME_ROUNDS = 3
VALUE_INTERVAL = 10


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def congrat_user(name):
    print(f'Congratulations, {name}!')


def play(game_name):
    name = welcome_user()
    if game_name():
        congrat_user(name)
    else:
        wrong_bye(name)


def get_rand_val(start_interval, end_interval):
    return random.randint(start_interval, end_interval)


def ask_answer(question_param):
    print(f'Question: {question_param}')
    answer = input('Your answer: ')
    return answer


def check_result(answer, right_answer):
    if right_answer == answer:
        print('Correct!')
        return True
    else:
        wrong_result(answer, right_answer)
        return False


def wrong_result(answer, result):
    print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{result}\'.')


def wrong_bye(name):
    print(f'Let\'s try again, {name}!')
