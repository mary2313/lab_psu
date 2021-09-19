from random import randint
a = []
N = int(input())
M = int(input())
col = []
row = []

min = 100
max = 0

print('\n')
for i in range(N):
    a.append([])
    count = 0
    for j in range(M):
        a[i].append(randint(0,6))
        count += a[i][j]
        if a[i][j] > max:
            max = a[i][j]
        if a[i][j] < min:
            min = a[i][j]
        print(a[i][j],end = '\t')
    row.append(count)
    print('\n')

count = 0

for i in range(M):
    for j in range(N):
        count += a[j][i]
    col.append(count)
    count = 0
print ('max = ', max)
print ('\nmin = ', min)
print ('\nrow = ', row)
print ('\ncol = ', col)
print('\n')



import random
class student():
    def __init__(self, ID, FirstName, LastName, faculty):
        self.ID = ID
        self.FirstName = FirstName
        self.LastName = LastName
        self.faculty = faculty
    def displayinfo(self):
        print (self.ID, self.FirstName, self.LastName, self.faculty)

Array = []
FirstNames = ["Никита","Алексей","Александр","Сергей","Евгений","Олег","Федор","Николай","Генадий","Борис"]
LastNames = ["Куприянов","Говядин","Лисов","Баклажанов","Бананов","Кузнецов","Мавродев","Мигеев","Фадеев","Богеев","Логеев","Сидоров","Шарапов","Бездный","мЫшь"]
facultys = ["ФВТ", "ФПТЭТ", "ФИТЭ"]

for i in range(20):
  Array.append(student(i+1,random.choice(FirstNames),random.choice(LastNames),random.choice(facultys)))
for i in range(len(Array)):
    print(" | ",Array[i].ID," | \t",Array[i].FirstName,'  '," \t|\t\t ",Array[i].LastName,' \t '," \t| ",Array[i].faculty," | ")

foundName = input('Имя?')
foundLastName = input('Фамилия?')
foundfaculty = input('Факультет?')

for i in range(len(Array)):
    if(Array[i].FirstName == foundName and Array[i].faculty == foundfaculty and Array[i].LastName == foundLastName):
        print(Array[i].displayinfo())