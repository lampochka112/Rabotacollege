import random

x = [random.randint(0, 9) for i in range(5)]

print("Список:", x)

c = sum(x)
print("Сумма элементов:", c)