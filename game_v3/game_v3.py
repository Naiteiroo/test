"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Инициализируем счётчик попыток, случайное число и шаг
    count = 0
    predict = np.random.randint(1, 101) 
    step = 20
    # Вызываем цикл, где проверяем является ли случайное число загаданным с корректировкой 
    while number != predict:
        count += 1
        if number > predict:
            predict += step
        elif number < predict:
            predict -= step
        if step > 1:
            step = step // 2

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


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)