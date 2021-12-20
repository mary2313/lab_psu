import random
import sys
G = []
c = []
N1 = int(input("First Matrix: "))
chance = [0,0,0,1,1,1,1,1,1,1]
for i in range(N1):
	G.append([])
	for j in range(N1):
		G[i].append(random.choice(chance))
		if(G[i][j] == 1):
			G[i][j] = random.randint(1,10)
		if(i == j):
			G[i][j] = 0
			
for i in range(N1):
	for j in range(N1):
		print(G[i][j],end='\t')
	print('\n')
print('\n'*3)

def BFS(v):
	vis[v] = 0
	queue.append(v)
	while(bool(queue)):
		s = queue[0]
		queue.pop(0)
		for i in range(len(G)):
			if(G[s][i] > 0 and vis[i] > vis[s] + G[s][i]):
				queue.append(i)
				vis[i] = vis[s] + G[s][i]

v = int(input('Вершина : ')) - 1

vis = []
for i in range(len(G)):
	vis.append(sys.maxsize)

queue = []

BFS(v)

for i in range(len(vis)):
	print(vis[i], end=' ')
input()