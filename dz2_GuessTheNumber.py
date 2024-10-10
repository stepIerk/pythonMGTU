import random
import os


def Menu():
    print('Чтобы выйти нажмите: E')
    print('Чтобы загадать новое число нажмите: R')


def MakeNewNomber():
    global nom
    nom = int(random.randint(1, 100))


def IsItNomber(ans):
    if ans.isdigit():
        return True
    return False


def Game(ans):
    if ans == 'R':
        MakeNewNomber()
        return ('Загадал новое число')
    elif IsItNomber(ans):
        return (Analizator(int(ans)))
    return ('Некоректные данные. Попробуйте снова')


def Analizator(ans):
    if ans > nom:
        return ('Многовато...')
    elif ans < nom:
        return ('Маловато...')
    return ('Угадал!')


MakeNewNomber()

while True:

    Menu()

    answer = input('введите число >>> ')
    if answer == "E":
        break

    print('<<< ' + Game(answer))

print('<<< Good Bye!')
os.system("say 'Good bye!'")
