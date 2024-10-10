
def is_prime(nom):
    for x in range(2, int(nom**(1/2)) + 1):
        if nom % x == 0:
            return "не простое"
    return "простое"

def prime_factores(nom):
    answer = []
    for x in range(1, int(nom/2) + 1):
        if nom % x == 0:
            if is_prime(x):
                answer.append(str(x))
    if is_prime(nom):
        answer.append(str(nom))
    return(answer)

def sqrt_sum(nom):
    summa = 0
    for i in range(1, nom+1):
        if is_prime(i):
            summa += i**2
    return(summa)
        