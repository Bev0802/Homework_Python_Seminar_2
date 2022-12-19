# Задайте список из n элементов, заполненных числами из промежутка [-n, n]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число списка последовательностей: "))
#Создание списка
if (n < 1): 
    print("Недопустимое число!")
    quit()
else: 
    l=(list(range(-n,n+1)))

#печать списка и его размера.
print(f"Список из промежутка [-{n}, {n}] -> {l}")

#Очистака файла перед записью
f = open('file.txt', 'w')
f.write('')
f.close()

#запись списка в file.txt по строчно. 
for i in range(len(l)):
    s = str(l[i]) 
    with open ("file.txt","a+") as f:
       if i < len(l)-1: f.write(f'{s}\n')
       else: f.write(f'{s}')

#чтение данных из file.txt и запись в список
path = 'file.txt'
data = open(path, 'r')
lis=[]
for i in data:
    i=i.replace("\n", "")
    lis.append(i)
data.close()
print(f"Список прочитанный из файла file.txt -> {lis}")

#Произведение списков записанное в новый список.
productLists = [0]
j=0
for i in range(len(l)):
    s = int(lis[j])
    p=l[i]*s
    productLists.append(p)
    j=j+1    

print(f"Произведение списков из файла из созданного по введенному числу n: {productLists}")

