import random
from brain_games.scripts.brain_games import rounds, interval
from brain_games import cli


def play_progression():
    max_len = 10  # максимальная длина случайной последовательности
    min_len = 5  # минимальная длина случайной последовательности
    max_step = 10  # максимальный шаг арифметической последовательности
    print('What number is missing in the progression?')
    for _ in range(rounds):  # запуск вопросов в количестве
        seq_len = random.randint(min_len, max_len)  # случайная длина
        seq_first_el = random.randint(1, interval)  # первый элекмент
        step = random.randint(1, max_step)  # случайный шаг
        seq = [str(seq_first_el)]
        val = seq_first_el
        # заполнение последовательности аоифметической прогрессии с шагом
        for i in range(seq_len):
            val += step
            seq.append(str(val))
        # исключение из последовательности случайного элемента
        take_away = random.randint(1, seq_len)
        rs = seq[take_away - 1]
        seq[take_away - 1] = '..'
        lst = ', '.join(seq)
        print(f'Question: {lst}')
        ans = input('Your answer: ')
        if rs == ans:
            print('Correct!')
        else:
            cli.wrong_res(ans, rs)
            return False
    return True
