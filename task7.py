# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
import random
N=int(input())
mas=[random.randint(-100,100) for i in range(N)]
print(mas)
mas0=[]
masN=[]
for i in range(N):
    if mas[i]>0:
        masN=[mas[i]]+masN
    elif mas[i]<0:
        masN.append(mas[i])
    else:
        mas0.append(0)
print(masN+mas0)