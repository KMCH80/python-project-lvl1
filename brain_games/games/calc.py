<<<<<<< HEAD
import random
from brain_games import cli


def play():
    print('What is the result of the expression?')
    for _ in range(cli.GAME_ROUNDS):
        num1 = random.randint(1, cli.VALUE_INTERVAL)
        num2 = random.randint(1, cli.VALUE_INTERVAL)
        set_exp = [f'{num1} + {num2}', f'{num1} - {num2}', f'{num1} * {num2}']
        exp = random.choice(set_exp)
        answer = cli.ask_answer(exp)
        result = eval(exp)
        if cli.check_result(int(answer), result):
            continue
        else:
            return True
    return True
||||||| parent of 27d83dd (Change)
=======
import random
from brain_games import cli


def play():
    print('What is the result of the expression?')
    for _ in range(cli.GAME_ROUNDS):
        num1 = random.randint(1, cli.VALUE_INTERVAL)
        num2 = random.randint(1, cli.VALUE_INTERVAL)
        set_exp = [f'{num1} + {num2}', f'{num1} - {num2}', f'{num1} * {num2}']
        exp = random.choice(set_exp)
        answer = cli.ask_answer(exp)
        result = eval(exp)
        if cli.check_result(int(answer), result):
            continue
        else:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            return False
=======
            return True
>>>>>>> d40d6ce0b1faefa156e967faca3c1bbc2558a91c
=======
            return True
>>>>>>> d40d6ce0b1faefa156e967faca3c1bbc2558a91c
=======
            return True
>>>>>>> d40d6ce0b1faefa156e967faca3c1bbc2558a91c
    return True
>>>>>>> 27d83dd (Change)
