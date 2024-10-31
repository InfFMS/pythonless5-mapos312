# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
import random
N=int(input())
mas=[random.randint(0,100) for i in range(N)]
mas1=mas[0:int(len(mas)/2)]
mas2=mas[int(len(mas)/2):len(mas)]
mas1.reverse()
mas2.reverse()
print(mas)
print(mas1+mas2)
