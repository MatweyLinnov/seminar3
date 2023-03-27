import random
from collections import Counter

a = int(input("Введите длину массива: "))
b=[random.randint(1, a) for i in range(a)]
print(b)

n = int(input("Искомое число: "))
melon = Counter(b)
#print(melon)

num = melon[n]
print(f"{num}")