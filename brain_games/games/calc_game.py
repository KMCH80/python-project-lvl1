import random
from brain_games.scripts.brain_games import rounds, interval
from brain_games import cli


def play_calc():
    print('What is the result of the expression?')
    for _ in range(rounds):
        num1 = random.randint(1, interval)
        num2 = random.randint(1, interval)
        seq = [f'{num1} + {num2}', f'{num1} - {num2}', f'{num1} * {num2}']
        op = random.choice(seq)
        print(f'Question: {op}')
        ans = input('Your answer: ')
        rs = eval(op)

        if rs == int(ans):
            print('Correct!')
        else:
            cli.wrong_res(ans, rs)
            return False
    return True
