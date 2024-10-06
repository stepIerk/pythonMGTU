
while True:
    year = int(input('Enter year >>> '))
    if year % 4 == 0:
        print('leap year')
    elif year == 0:
        print('Exit...')
        break
    else:
        print('not leap year')
    