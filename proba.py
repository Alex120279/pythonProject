import math


# находим среднее значение
def find_average(x):
    return sum(x) / len(x)


# находим дисперсию
def find_dispersion(x):
    d = 0
    for i in x:
        d += (find_average(x) - i) ** 2
    return d


# находим среднеквадратичное отклонение
def root_mean_square_deviation(x):
    return math.sqrt(find_dispersion(x) / ((len(a)) - 1))


a = list(map(int, "1 5 2 7 1 9 3 8 5 9".split()))

print(root_mean_square_deviation(a))
