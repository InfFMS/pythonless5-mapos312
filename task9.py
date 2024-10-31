# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
import random
N=int(input())
nums=[]
mas=[random.randint(0,1000) for i in range(N)]
print(mas)
for i in range (N):
    a=0
    for x in range(len(nums)):
        if nums[x]==mas[i]:
            a=1
            break
    if a==0:
        nums.append(mas[i])
print(nums)