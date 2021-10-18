import random

def CreateTwoMatrix():
	global M1
	global M2
	global N1
	global N2
	M1 = []
	M2 = []
	N1 = int(input("First Matrix: "))
	N2 = int(input("Second Matrix: "))
	chance = [0,0,0,1,1,1,1,1,1,1]
	#Шанс 1 - 70%
	#Шанс 0 - 30%

	#Создание 2 матриц смежности неориентированных помеченных графов 
	# № 1
	for i in range(N1):
		M1.append([])
		for j in range(N1):
			M1[i].append(random.choice(chance))
			if(i == j):
				M1[i][j] = 0
			
	for i in range(N1):
		for j in range(N1):
			M1[i][j] = M1[j][i]
			print(M1[i][j],end='\t')
		print('\n')
	print('\n'*3)
	# № 2

	for i in range(N2):
		M2.append([])
		for j in range(N2):
			M2[i].append(random.choice(chance))
			if(i == j):
				M2[i][j] = 0
			
	for i in range(N2):
		for j in range(N2):
			M2[i][j] = M2[j][i]
			print(M2[i][j],end='\t')
		print('\n')
	print('\n'*3)

def combineGraphs(M1,M2):

	if(len(M1) < len(M2)):
		M1, M2 = M2, M1
	G = []
	for i in range(len(M1)):
		G.append([])
		for j in range(len(M1)):
			try:
				if(M1[i][j] or M2[i][j]):
					G[i].append(1)
				else:
					G[i].append(0)
			except IndexError:
				G[i].append(M1[i][j])
	return G
		

def confluence(M1,M2):

	if(len(M1) < len(M2)):
		M1, M2 = M2, M1
	G = []
	for i in range(len(M1)):
		G.append([])
		for j in range(len(M1[i])):
			try:
				if(M1[i][j] and M2[i][j]):
					G[i].append(1)
				else:
					G[i].append(0)

			except IndexError:
				G[i].append(0)
			
	return G
	
def annularSum(M1,M2):
	if(len(M1) < len(M2)):
		M1, M2 = M2, M1
	G = []
	for i in range(len(M1)):
		G.append([])
		for j in range(len(M1[i])):
			try:
				if((M1[i][j] == 1 and M2[i][j] == 0) or (M2[i][j] == 1 and M1[i][j] == 0)):
					G[i].append(1)
				else:
					G[i].append(0)
			except IndexError:
				G[i].append(M1[i][j])
	return G


CreateTwoMatrix()
# Объединение графов
#G = combineGraphs(M1,M2)
#print("Объединение графов:", '\n')
# Пересечение
#G = []
#print("Пересечение:", '\n')
#G = confluence(M1,M2)

# Кольцевая сумма
G = []
print("кольцевая сумма:", '\n')
G = annularSum(M1,M2)

for i in range(len(G)):
	for j in range(len(G[i])):
		print(G[i][j],end='\t')
	print('\n')
print('\n'*3)