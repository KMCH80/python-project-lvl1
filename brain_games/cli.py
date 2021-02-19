import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def congrat_user(name):
    print(f'Congratulations, {name}!')


def wrong_bye(name):
    print(f'Let\'s try again, {name}!')
