import prompt


# привестствие игрока и получение его имени
def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# поздравление игрока (по имени) с выигранной игрой
def congrat_user(name):
    print(f'Congratulations, {name}!')


# объявление о неправильном ответе с указанием ответов
def wrong_res(ans, rs):
    print(f'\'{ans}\' is wrong answer ;(. Correct answer was \'{rs}\'.')


# Прощание с игроком при неправильном ответе
def wrong_bye(name):
    print(f'Let\'s try again, {name}!')
