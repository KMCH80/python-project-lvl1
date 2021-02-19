import random
from brain_games.scripts.brain_games import levels, interval


def play_even():
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    for _ in range(levels):
        num = random.randint(1, interval)
        print('Question:', str(num))
        ans = input('Your answer: ')

        if (num % 2 and ans == 'no') or (num % 2 == 0 and ans == 'yes'):
            print('Correct!')
        else:
            if num % 2:
                rl = 'no'
            else:
                rl = 'yes'
            print(f'\'{ans}\' is wrong answer ;(. Correct answer was \'{rl}\'.')
            return False
    return True
