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

CreateTwoMatrix()

M11 = M1.copy()
M22 = M2.copy()


'''------------------------------------------------------ 2 задание
№ 1 - Отождествление вершин
'''
print("№1\n a) Отождествление вершин\n")

a1 = int(input('Первая вершина : ')) - 1
a2 = int(input('Вторая вершина : ')) - 1

def identification(M1,a1,a2):
    
    if(a1 > a2):
        Max = a1
        Min = a2
    else:
        Max = a2
        Min = a1

    G = []
    for i in range(N1):
        G.append(M1[Min][i] + M1[Max][i])
        if(G[i] == 2):
            G[i] = 1

    for i in range(N1):
        M1[Min][i] = G[i]
        M1[i][Min] = G[i]

    for i in range(N1-1):
        for j in range(N1-1):
            if(i >= Max):
                M1[i][j] = M1[i+1][j]
            elif(j >= Max):
                M1[i][j] = M1[i][j + 1]
            if(i >= Max and j >= Max):
                M1[i][j] = M1[i + 1][j + 1]


    return M1


G = identification(M1,a1,a2)
for i in range(len(G)-1):
    for j in range(len(G)-1):
        print(G[i][j],end="\t")
    print("\n")
print("\n"*3)

print("№1\n б) Стягивание вершин\n")

M1 = M11.copy()
def constriction(M1,a1,a2):
    if(M1[a1][a2] != 1):
        print("Выберите другие вершины, эти не связанные")
        return 0
    F = identification(M1,a1,a2)
    for i in range(len(F)-1):
        for j in range(len(F)-1):
            if(i == j):
                F[i][j] = 0
    return F
F=0
while(F==0):
    a1 = int(input('Первая вершина : ')) - 1
    a2 = int(input('Вторая вершина : ')) - 1
    F = constriction(M1,a1,a2)
for i in range(len(F)-1):
    for j in range(len(F)-1):
        print(F[i][j],end="\t")
    print("\n")
print("\n"*3)

print("№1\n в) Расщепление вершин во сторой матрице\n")

a1 = int(input('Расщепить вершину под номером : \n')) - 1

M2.append(M2[a1].copy())
for i in range(len(M2)-1):
    M2[i].append(M2[i][a1])

M2[a1][len(M2)-1] = M2[len(M2)-1][a1] = 1

M2[len(M2)-1].append(0)

for i in range(len(M2)):
    for j in range(len(M2[i])):
        print(M2[i][j],end='\t')
    print('\n')
print('\n'*3)
