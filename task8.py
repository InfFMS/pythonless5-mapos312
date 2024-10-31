# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
import random

def z(num):
    string=str(num)
    x=0
    for i in range(1,len(string)):
        if string[i]!=string[i-1]:
            x=1
            break
    if x==1: return False
    else: return True
N=int(input())
mas=[random.randint(10,10000) for i in range(N)]
print(mas)
nums=[]
for i in range(N):
    if z(mas[i]):
        nums.append(mas[i])
print(nums)