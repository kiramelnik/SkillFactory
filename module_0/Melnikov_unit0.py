import numpy as np

number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")


def game_core_v3(number):
    count = 1
    lower_limit = 1
    upper_limit = 101
    predict = 50  # Начинаем угадывание с середины возможного диапазона
    while predict != number:  # Условие, при котором функция будет выполняться пока предположение не будет равным
        # загаданному числу
        if predict > number:
            upper_limit = predict
        else:
            lower_limit = predict
        count += 1  # Прибавляем единицу к счётчику каждый раз, когда цикл проходит круг
        predict = lower_limit + (upper_limit - lower_limit) // 2  # Присваиваем predict новое значение по формуле
        # бинарного поиска
    return count  # Выход из функции при нахождении нужного числа и вывод количества попыток


def score_game(game_core_v3):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)
