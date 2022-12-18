# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

def SumDigitsRealNumber(a):                              #Функция, которая принимает вещественное число любой длинны как до запятой так и после и считает сумму цифр в этом числе.
        s=0                                              #Переменная для хранения и вывода суммы использования в сумме
        ch = a.find(",")
        if ch == -1:
                a = int(a)
                result = a
                while (result > 0):
                        s = (result % 10) + s
                        result = result // 10
                print(s)       
        else:
                list_str = a.split(",")                  #Преобразуем строку в список c помощью .split
                #str_a = "".join(list_str)               #Преобразуем список в стоку с помощью .join

                for i in range (0, len(list_str)-1):    #Преобзазование списка в строку с помощью цикла
                        for j in range (1, len(list_str)):
                                list_str = list_str[i] + list_str[j]
                print(list_str)
        
                for i in range (0,len(list_str)):       #Суммируем цифры в строке
                        n = int(list_str[i])        
                        s=s+n
                print(s)

num = input("Введите вещественное число, отделяя дробную часть от челого числа точкой ',': ")
print(num)
SumDigitsRealNumber(num)