from brain_games import cli
from brain_games.games import even, calc, gcd, prime, progression  # noqa: F401

GAME_ROUNDS = 3
VALUE_INTERVAL = 100


def start_game(game_name):
    f = globals()[game_name]
    user_name = cli.welcome_user()
    f.tell_rules()
    for _ in range(GAME_ROUNDS):
        task_with_right_answer = f.get_task_with_right_answer(VALUE_INTERVAL)
        answer = say_ask_answer(task_with_right_answer[0])
        if check_result(answer, task_with_right_answer[1]):
            say_ok()
        else:
            say_wrong_result(answer, task_with_right_answer[1])
            say_bye(user_name)
            return
    say_congrat_winner(user_name)


def say_ask_answer(question_param):
    print(f'Question: {question_param}')
    answer = input('Your answer: ')
    return answer


def check_result(answer, right_answer):
    if right_answer == answer:
        return True
    else:
        return False


def say_ok():
    print('Correct!')


def say_congrat_winner(name):
    print(f'Congratulations, {name}!')


def say_wrong_result(ansr, right_res):
    print(f'\'{ansr}\' is wrong answer ;(. Correct answer was \'{right_res}\'.')


def say_bye(name):
    print(f'Let\'s try again, {name}!')
