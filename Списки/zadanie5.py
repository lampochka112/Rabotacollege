import random

x = [random.randint(0, 20) for _ in range(10)]
print("Исходный список:", x)

c = x.copy()

for i in range(len(c)):
    if c [i] % 2 != 0:
        c [i] = 0

print("Измененный список:", c)