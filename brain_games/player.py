import prompt

GAME_ROUNDS = 3


def start_game(game_module):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.RULES)
    for _ in range(GAME_ROUNDS):
        task, right = game_module.get_task_with_right_answer()
        answer = say_ask_answer(task)
        if answer == right:
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{right}\'.')
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')


def say_ask_answer(question_param):
    print(f'Question: {question_param}')
    answer = prompt.string('Your answer: ')
    return answer
