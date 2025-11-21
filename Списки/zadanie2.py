n = int(input("Введите количество писателей: "))
pisateli = []
for i in range(n):
    surname = input(f"Введите фамилию писателя {i+1}: ")
    pisateli.append(surname)
pisateli.sort()
print("Отсортированный список фамилий писателей:")
for pisateli in pisateli:
    print(pisateli)