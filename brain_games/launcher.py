import prompt

NUMBER_OF_ROUNDS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        task, right_answer = game.get_task_with_right_answer()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f" Correct answer was '{right_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
