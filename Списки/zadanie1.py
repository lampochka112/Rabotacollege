# Ваш список любимых фильмов
movies = ["Интерстеллар", "Начало", "Матрица", "Побег из Шоушенка"]

# а) в строчку
movies_inline = " ".join(movies)
print("а) в строчку:", movies_inline)

# б) в столбик
print("б) в столбик:")
for movie in movies:
    print(movie)

# в) в строчку через запятую
movies_comma = ", ".join(movies)
print("в) в строчку через запятую:", movies_comma)