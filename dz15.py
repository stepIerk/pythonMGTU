import math as m
def prime(nom):
    for x in range(2, int(m.sqrt(nom)) + 1):
        if nom % x == 0:
            return False
    return True

for i in range(1, 100):
    if prime(i) == True:
        print(i)