import random
G = []
c = []
N1 = int(input("First Matrix: "))
chance = [0,0,0,1,1,1,1,1,1,1]
for i in range(N1):
    G.append([])
    for j in range(N1):
        G[i].append(random.choice(chance))
        if(i == j):
            G[i][j] = 0
            
for i in range(N1):
    for j in range(N1):
        G[i][j] = G[j][i]
        print(G[i][j],end='\t')
    print('\n')
print('\n'*3)

def BFSD(v):
    Vis[v] = 1
    queue.append(v)
    while(bool(queue)):
        s = queue[0]
        
        queue.pop(0)
        for i in range(len(G)):
            if(G[s][i] == 1 and Vis[i] == -1):
                queue.append(i)
                Vis[i] = 1 + Vis[s]


queue = []
Vis = []
for i in range(len(G)):
    Vis.append(-1)

v = int(input('\nВершина : ')) - 1
print("\n")
BFSD(v)

for i in range(len(Vis)):
    print(i+1 ,' : ' , Vis[i] - 1)

print("---список смежности---")

for i in range(len(G)):
    c.append([]) 
    for j in range(len(G[i])):
        if(G[i][j] == 1):
            c[i].append(j)
    print("\n",i+1," - ",end='')
    for j in range(len(c[i])):
        print(c[i][j]+1, end=' ')

def BFSD1(v1):
    Vis1[v1] = 1
    queue1.append(v1)
    while(bool(queue1)):
        s = queue1[0]
        
        queue1.pop(0)
        for i in range(len(c[s])):
            if(Vis1[c[s][i]] == -1):
                queue1.append(c[s][i])
                Vis1[c[s][i]] = 1 + Vis1[s]

print('\n')

v1 = int(input('Вершина : ')) - 1

Vis1 = []
for i in range(len(c)):
    Vis1.append(-1)

queue1 = []

BFSD1(v1)

for i in range(len(Vis1)):
    print(i+1 ,' : ' , Vis1[i] - 1)


def DFS(v):
    print(v + 1)
    vis[v] = 1
    for i in range(len(G)):
        if(G[v][i] == 1 and vis[i] == 0):
            DFS(i)

v = int(input("Вершина: ")) - 1
vis = []
for i in range(len(G)):
    vis.append(0)

DFS(v)