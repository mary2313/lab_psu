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



def Decart(M1,M2):
	G = []
	count = -1
	for i in range(len(M1)):
		for j in range(len(M2)):
			G.append([])
			count += 1
			for ii in range(len(M1)):
				for jj in range(len(M2)):
					if(i == jj and j == ii):
						G[count].append(0)
					elif(i == ii):
						G[count].append(M2[j][jj])
					elif(j == jj):
						G[count].append(M1[i][ii])
					else:
						G[count].append(0)

	return G










CreateTwoMatrix()
G = Decart(M1,M2)

for i in range(len(G)):
	for j in range(len(G[i])):
		print(G[i][j],end="\t")
	print("\n")