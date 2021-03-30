import random


a = []
b = []

# заполнение массива рандомными числыми
n, m = map(int, input().split())
for i in range(n):
   a.append([random.randint(0,10) for j in range(m)])

#проход по стобцам
for i in range(m):
    pr = 1
    for j in range(n):
        pr*=a[j][i]
    b.append(pr) #занесение полученнного значения в новый массив
        
#вывод начального двумерного массива
for i in range(n):
    for j in range(m):
        print("%4d" % a[i][j], end = " ")
    print()

print()

#вывод полученного одномерного массива
for i in b:
    print ("%4d" % i, end = " ")