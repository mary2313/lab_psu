import random
import sys
import os

INPUT = sys.argv

orintation = False
weighted = False
N1 = 0
v = 0
def InputParams():
	global N1
	global orintation
	global weighted
	global v
	for i in range(len(INPUT)):
		try:
			print(INPUT[i])
			INPUT[i] = INPUT[i].upper()
			if(INPUT[i] == "ОРИЕНТИРОВАННАЯ" or INPUT[i] == "ОРИНТИРОВАННАЯ" or INPUT[i] == "ОРИЕНТИРОВАНАЯ" or INPUT[i] == "ОРЕНТИРОВАННАЯ" or INPUT[i] == "ЕСТЬ ОРИЕНТАЦИЯ"):
				orintation = True
			if(INPUT[i] == "ВЗВЕШЕННАЯ" or INPUT[i] == "ВЗВЕШЕНАЯ" or INPUT[i] == "ВЗВЕЩЕННАЯ" or INPUT[i] == "ВЗВЕШИННАЯ" or INPUT[i] == "ВЗВЕШИНАЯ"):
				weighted = True
			if(N1 == 0):
				N1 = int(INPUT[i])
			else:
				v = int(INPUT[i]) - 1
		except ValueError:
			continue

InputParams()

G = []
c = []

chance = [1,1,1,1,1,1,1,0,0,0]
for i in range(N1):
	G.append([])
	for j in range(N1):
		G[i].append(random.choice(chance))
		if(weighted):
			if(G[i][j] == 1):
				G[i][j] = random.randint(1,10)
		if(i == j):
			G[i][j] = 0
			
for i in range(N1):
	for j in range(N1):
		if(orintation == False):
			G[i][j] = G[j][i]
		print(G[i][j],end='\t')
	print('\n')
print('\n'*3)


def BFS(v):
	vis[v] = 0
	queue.append(v)
	while(bool(queue)):
		s = queue[0]
		#print(s+1)
		queue.pop(0)
		for i in range(len(G)):
			if(G[s][i] > 0 and vis[i] > vis[s] + G[s][i]):
				queue.append(i)
				vis[i] = vis[s] + G[s][i]

vis = []
for i in range(len(G)):
	vis.append(sys.maxsize)

queue = []

BFS(v)

for i in range(len(vis)):
	if(vis[i] == sys.maxsize):
		print("Вершина ", i + 1, "изолированная")
		vis[i] = 0
	
print("Расстояния от вершины ", v + 1 , "\n")
for i in range(len(vis)):
	print(vis[i], end=' ')

input()