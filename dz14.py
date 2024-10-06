nom = int(input('Enter nomber >>> '))
for i in range(1, nom//2 + 1):
    if nom % i == 0:
        print(i, '*', int(nom/i), '=', nom)
