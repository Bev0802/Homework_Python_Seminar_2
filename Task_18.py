# Реализуйте алгоритм перемешивания списка.
import random

list = list(range(1,50,7))
print(list)

random.shuffle(list)
print(list)

quit()
def random_int(num):
    rand = datetime.datetime.now().microsecond/10**6
    return int(num*rand)

a = [1,2,3,4,5,6]
print(a)
random_int(5)
for i in range(len(a)-1,-1,-1):
    j = random_int(i+1)
    a[i],a[j] = a[j],a[i]
print(a)
