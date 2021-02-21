import random
from brain_games.scripts.brain_games import levels, interval
from brain_games import cli


def play_gcd():
    print('Find the greatest common divisor of given numbers.')
    for _ in range(levels):
        k = random.randint(2, interval)
        m = random.randint(2, interval)
        num1 = random.randint(2, interval)
        num2 = num1 * k
        num1 = num1 * m
        rs = 1
        for i in range(num1, 1, -1):
            if num1 % i or num2 % i:
                continue
            else:
                rs = i
                break
        print(f'Question: {num1} {num2}')
        ans = input('Your answer: ')
        if rs == int(ans):
            print('Correct!')
        else:
            cli.wrong_res(ans, rs)
            return False
    return True
