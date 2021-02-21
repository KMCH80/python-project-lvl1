import random
from brain_games.scripts.brain_games import rounds, interval
from brain_games import cli


def play_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(rounds):
        num = random.randint(2, interval)
        print('Question:', str(num))
        ans = input('Your answer: ')
        rs = 'yes'
        for i in range(num - 1, 1, -1):
            if num % i:
                continue
            else:
                rs = 'no'
                break
        if ans == rs:
            print('Correct!')
        else:
            cli.wrong_res(ans, rs)
            return False
    return True
