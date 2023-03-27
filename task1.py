import random
from collections import Counter

a = int(input("Введите длину массива: "))
b=[random.randint(1, a) for i in range(a)]
print(b)

n = int(input("Искомое число: "))
counter = Counter(b)
#print(melon)

num = counter[n]
print(f"Искомого числа в массиве - {num}")