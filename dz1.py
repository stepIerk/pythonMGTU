
# 1
print(int(input('Первое число для сложения: ')) +
      int(input('Второе число для сложения: ')))

# 2
print(int(str(input('Перевести строку в число: '))))
print(str(int(input('Перевести число в строку: '))))

# 3
print(float(input('ширина: ')) * float(input('высота: ')))

# 4
print(int(input('делимое: ')) % int(input("делитель: ")))

# 5
# a
a, b = map(int, input(
    'Введите два числа чтобы поменять местами через пробел: ').split())
c = a
a = b
b = c
print(a, b)

# b
a, b = map(int, input(
    'Введите два числа чтобы поменять местами через пробел: ').split())
a, b = b, a
print(a, b)
