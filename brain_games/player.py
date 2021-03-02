import prompt

GAME_ROUNDS = 3


def start_game(game_module):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.RULES)
    for _ in range(GAME_ROUNDS):
        task, right = game_module.get_task_with_right_answer()
        ans = say_ask_answer(task)
        if ans == right:
            print('Correct!')
        else:
            s = f'\'{ans}\' is wrong answer ;(. Correct answer was \'{right}\'.'
            print(s)
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')


def say_ask_answer(question_param):
    print(f'Question: {question_param}')
    answer = prompt.string('Your answer: ')
    return answer
