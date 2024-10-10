import dz2aboutPrime as f

print(f.is_prime(int(input('введите число чтобы проверить простое ли оно >>> '))))
print(' '.join(f.prime_factores(int(input('введите число чтобы получить его простые делители >>> ')))))
print(f.sqrt_sum(int(input('введите число чтобы получить сумму квадратов простых чисел до него >>> '))))
print('это все что я могу')