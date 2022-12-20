# Задайте список из n элементов, заполненных числами из промежутка [-n, n]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input("Введите число списка последовательностей: "))
#Создание списка
if (n < 1): 
    print("Недопустимое число!")
    quit()
else: 
    l=(list(range(-n,n+1)))

#печать списка и его размера.
print(f"Список из промежутка [-{n}, {n}] -> {l}")
print (f"Длинна списка {len(l)}")


#Очистака файла перед записью
f = open('file.txt', 'w')
f.write('')
f.close()

#запись индексов списка произволь в file.txt по строчно.
lens = int(len(l)/2)
if (lens%2)!= 0:
        lens=lens-1

for i in range(lens):
    s = random.randrange(len(l))
    s = str(s) 
    with open ("file.txt","a+") as f:
        f.write(f'{s}\n')
       

#чтение данных из file.txt и запись в список
path = 'file.txt'
data = open(path, 'r')
lis=[]
for i in data:
    i=i.replace("\n", "")
    lis.append(i)
data.close()
print(f"Список индексов прочитанный из файла file.txt -> {lis}")

#Произведение списка l созданного послеввода, по индексам взятыми из файла.
productLists = []
p=0
j=1
for i in range(0,len(lis)-1,2):
        a = int(lis[i])
        b = int(lis[j])
        j= j+2
        p = (l[a])*(l[b])
        print(f"{l[a]}*{l[b]}={p}")
        productLists.append(p)    
       
print(f"Произведение чисел списка [-n, n] по индексам взятым из файла: {productLists}")