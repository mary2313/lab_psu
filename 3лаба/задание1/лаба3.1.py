import random

a = []
b = []
c = []
d = []
N = int(input())
M = int(input())
change = ['| |','| |','| |','|1|','|1|','|1|','|1|','|1|','|1|','|1|']

#задание 1:

print('\n')
print('№1')

for i in range(N):
    a.append([])
    for j in range(N):
        a[i].append(random.choice(change))
        if(i == j):
            a[i][j] = '| |'
       
print('\n')

for i in range(N):
    for j in range(N):
        a[i][j] = a[j][i]
        print(a[i][j],end = '\t')
    print('\n')

print('\n')
print('№2')

for i in range(M):
    b.append([])
    for j in range(M):
        b[i].append(random.choice(change))
        if(i == j):
            b[i][j] = '| |'
       
print('\n')

for i in range(M):
    for j in range(M):
        b[i][j] = b[j][i]
        print(b[i][j],end = '\t')
    print('\n')

print('список смежности №1', '\n')

for i in range(N):
    c.append([])
    for j in range(N):
        if(a[i][j] == '|1|'):
            c[i].append(j)
print(c,'\n')

print('список смежности №2', '\n')

for i in range(M):
    d.append([])
    for j in range(M):
        if(b[i][j] == '|1|'):
            d[i].append(j)
print(d)

#задание 2




input()