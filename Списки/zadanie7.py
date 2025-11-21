import random
a = [random.randint(1,10) for i in range(1,10)]
b = []
for i in a:
    if i < 5:
        b.append(i)
print(f'a = {a}\n'
      f'b = {b}')