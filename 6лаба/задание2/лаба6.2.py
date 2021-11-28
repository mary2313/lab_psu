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

for i in range(len(G)):
    for j in range(len(G[i])):
        G[i][j] = G[j][i]
        print(G[i][j],end='\t')
    print('\n')

def DFS(v, count):
    vis[v] = count
    for i in range(len(G)):
        if(G[v][i] == 1 and vis[i] == -1):
            DFS(i,count + 1)
        if(G[v][i] == 1 and vis[i] > count):
            DFS(i,count + 1)
    
            
v = int(input("\nВершина: ")) - 1
vis = []
for i in range(len(G)):
    vis.append(-1)

count = 0           
DFS(v,count)
print("\n")

for i in range(len(vis)):
    print(i+1,' : ' , vis[i])

print("---список смежности---")

for i in range(len(G)):
    c.append([]) 
    for j in range(len(G[i])):
        if(G[i][j] == 1):
            c[i].append(j)
    print("\n",i+1," - ",end='')
    for j in range(len(c[i])):
        print(c[i][j]+1, end=' ')
print("\n")

def DFS1(v,count):
    vis[v] = count
    for i in range(len(c[v])):
        if(vis[c[v][i]] == -1):
            DFS(c[v][i],count + 1)
        if(vis[c[v][i]] > count):
            DFS(c[v][i],count + 1)

v = int(input("\nВершина: ")) - 1

for i in range(len(vis)):
    vis[i] = -1
count = 0           

DFS1(v,count)

print("\n")
for i in range(len(vis)):
    print(i+1,' : ' , vis[i])
