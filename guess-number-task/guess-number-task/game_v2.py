"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число, используя бинарный поиск

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    lower_bound = 1
    upper_bound = 100
    next_step = 0

    while True:
        count += 1
        predict_number = lower_bound + next_step if upper_bound - lower_bound == 1 else int((lower_bound + upper_bound) / 2) # предполагаемое число

        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            lower_bound = predict_number
            next_step = 1
        else:
            upper_bound = predict_number
            next_step = 0

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
