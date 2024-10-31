# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
import random
import math
# Функция для длины вектора
def L(v):
    return math.sqrt(sum(x**2 for x in v))
# Функция для скалярного произведения
def DP(a, b):
    return sum(x * y for x, y in zip(a, b))
N = int(input())
# Генерим вектора
a = [random.randint(-10, 10) for _ in range(N)]
b = [random.randint(-10, 10) for _ in range(N)]
print("вектор a:", a)
print("вектор b:", b)
# Вычисляем
dp = DP(a, b)
la = L(a)
lb = L(b)
if la == 0 or lb == 0:
    print("Не может быть")
else:
    cos = dp / (la * lb)
    cos = max(min(cos, 1), -1)  # Ограничение для cos(alpha)
    alpha_rad = math.acos(cos)
    alpha_deg = math.degrees(alpha_rad)
    print("Угол (градусы:", alpha_deg)