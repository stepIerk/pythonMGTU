nom = input('enter nomber >>> ')
if nom[::-1] == nom:
    print(nom, '- palindrom')
else:
    print(nom, '- not palindrom')
    