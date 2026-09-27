# dragon4
""драконы""
Задача про драконов
def max_dragon_power(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 4  # 2*2 = 4

    # Для N >= 5 используем жадный алгоритм с тройками
    power = 1
    while n > 4:
        power *= 3
        n -= 3
    
    # Оставшееся число (2, 3 или 4) умножаем
    power *= n
    return power


if __name__ == "__main__":
    # Пример из задания
    N = 12
    result = max_dragon_power(N)
    print(f"Суммарное количество голов: {N}")
    print(f"Максимальная сила стаи: {result}")
