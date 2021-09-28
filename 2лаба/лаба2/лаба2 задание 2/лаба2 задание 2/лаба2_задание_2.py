import time
import random 

def shellSort(data, length):
    gap = length//2
    while gap > 0:            
        for i in range(gap, length):
            temp = data[i]
            j = i
            while(j >= gap and data[j - gap] > temp):
                data[j] = data[j - gap]
                j -= gap   
            data[j] = temp
        gap //= 2
    

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quickSort(s_nums) + e_nums + quickSort(m_nums)

#случайные
data1 = []
for i in range(1000000):
    data1.append(random.randint(0,100000))

data2 = data1.copy()
data3 = data1.copy()

starttime = time.time()
shellSort(data1, len(data1))
endtime = time.time()
print("\n\n--Сортировка cо cлучайными числами--")
print("\nСортировка Шелла")
print(endtime - starttime)
print("\n")

starttime = time.time()
quickSort(data2)
endtime = time.time()
print("\nБыстрая сортировка")
print(endtime - starttime)
print("\n")

starttime = time.time()
data3.sort()
endtime = time.time()
print("\nСтандартная сортировка py")
print(endtime - starttime)

#возрастающие
data1 = []

for i in range(1000000):
    data1.append(i) 
data2 = data1.copy()
data3 = data1.copy()

starttime = time.time()
shellSort(data1, len(data1))
endtime = time.time()
print("\n\n--Сортировка с возрастающими числами--")
print("\nСортировка Шелла")
print(endtime - starttime)
print("\n")

starttime = time.time()
quickSort(data2)
endtime = time.time()
print("\nБыстрая сортировка")
print(endtime - starttime)
print("\n")

starttime = time.time()
data3.sort()
endtime = time.time()
print("\nСтандартная сортировка py")
print(endtime - starttime)

#убывающие
data1 = []

for i in range(1000000):
    data1.append(1000000-i) 
data2 = data1.copy()
data3 = data1.copy()

starttime = time.time()
shellSort(data1, len(data1))
endtime = time.time()
print("\n\n--Сортировка с убывающими числами--")
print("\nСортировка Шелла")
print(endtime - starttime)
print("\n")

starttime = time.time()
quickSort(data2)
endtime = time.time()
print("\nБыстрая сортировка")
print(endtime - starttime)
print("\n")

starttime = time.time()
data3.sort()
endtime = time.time()
print("\nСтандартная сортировка py")
print(endtime - starttime)

#смешанная
data1 = []

for i in range(int(1000000/2)):
    data1.append(i)
for i in range(int(1000000/2)):
    data1.append(1000000-i)
data2 = data1.copy()
data3 = data1.copy()

starttime = time.time()
shellSort(data1, len(data1))
endtime = time.time()
print("\n\n--Сортировка с смежными числами--")
print("\nСортировка Шелла")
print(endtime - starttime)
print("\n")

starttime = time.time()
quickSort(data2)
endtime = time.time()
print("\nБыстрая сортировка")
print(endtime - starttime)
print("\n")

starttime = time.time()
data3.sort()
endtime = time.time()
print("\nСтандартная сортировка py")
print(endtime - starttime)
input()