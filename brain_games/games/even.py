<<<<<<< HEAD
import random
from brain_games import cli


def play():
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    for _ in range(cli.GAME_ROUNDS):
        number = random.randint(1, cli.VALUE_INTERVAL)
        answer = cli.ask_answer(str(number))
        if number % 2:
            result = 'no'
        else:
            result = 'yes'
        if cli.check_result(answer, result):
            continue
        else:
            return True
    return True
||||||| parent of 27d83dd (Change)
=======
import random
from brain_games import cli


def play():
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    for _ in range(cli.GAME_ROUNDS):
        number = random.randint(1, cli.VALUE_INTERVAL)
        answer = cli.ask_answer(str(number))
        if number % 2:
            result = 'no'
        else:
            result = 'yes'
        if cli.check_result(answer, result):
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
