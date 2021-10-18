import random
G = []
v = []
v1 = []
N = 5
M = 5
c = []
change = [0,0,0,1,1,1,1,1,1,1]

for i in range(N):
    G.append([])
    for j in range(N):
        G[i].append(random.choice(change))
        if(i == j):
            G[i][j] = 0
       
print('\n')

for i in range(N):
    for j in range(N):
        G[i][j] = G[j][i]
        print(G[i][j],end = '\t')
    print('\n')

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
print('\n')

print("---список смежности---")
#---список смежности---

for i in range(len(G)):
    c.append([]) 
    for j in range(len(G[i])):
        if(G[i][j] == 1):
            c[i].append(j)
    print("\n",i+1," - ",end='')
    for j in range(len(c[i])):
        print(c[i][j]+1, end=' ')

def DFS1(v1):
    print(v1 + 1)
    vis[v1] = 1
    for i in range(len(c[v1])):
        if(vis[c[v1][i]] == 0):
            DFS1(c[v1][i])

v1 = int(input("\n Вершина: ")) - 1
vis = []
for i in range(len(c)):
    vis.append(0)

DFS1(v1)

input()