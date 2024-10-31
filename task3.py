# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3
import random
x=0
N=int(input())
mas=[random.randint(0,100) for i in range(N)]
#print(mas)
for i in range(100):
    string=""
    for q in range(N):
        if mas[q]==i:
            string+=str(q)+' и '
    if string!='' and len(string.split())>2:
        print("значение"+str(i)+":"+string[0:len(string)-3])
        x+=1
if x==0:
    print("Нет")

