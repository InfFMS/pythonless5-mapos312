# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
N=list(map(int,input().split()))
count=0
for i in range(len(N)):
    if N[i]==max(N):
        count+=1
print(count)