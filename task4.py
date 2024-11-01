# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
import random as r
# Функция для генерации массива
def x(N):
    return [r.randint(0, 1000) for _ in range(N)]
# Функция для отфильтровывания
def e(i):
    m = sum(i) / len(i)
    t = m * 0.3
    return [x for x in i if abs(x - m) <= t]
N = int(input())
a = x(N)
print("Сгенерированный массив:", a)
f_a = e(a)
print("Отфильтрованный массив:", f_a)