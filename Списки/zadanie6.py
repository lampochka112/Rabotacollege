import random
a = [random.randint(-100,101)
for i in range(10)]
print(*a)
for num in range(10):
    for i in range(0, 9, 1):
        if a[i] > 0 and a[i+1] < 0:
            a[i],a[i+1] = a[i+1],a[i]
print(*a)