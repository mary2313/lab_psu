import time
from random import randint
start_time = time.time() 

a = []
b = []
c = []
N = int(input())
M = int(input())

print('\n')

for i in range(N):
    a.append([])
    for j in range(M):
        a[i].append(randint(0,100))
    print('\n')

print('\n')

for i in range(N):
    b.append([])
    for j in range(M):
        b[i].append(randint(0,100))
    print('\n')

for i in range(N):
	c.append([])	
	for j in range(M):
		c[i].append(a[i][j] * b[i][j])
print('\n')
print("%s" % (time.time() - start_time))