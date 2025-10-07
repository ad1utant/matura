import math
from importlib.metadata import pass_none


def funkcja(k):
    pom = k
    length = 0
    zera = 1
    while True:
        k//= 10
        length+=1
        if k == 0:
            break
    for j in range(length//2):
        zera *= 10
    a = pom//zera
    b = pom%zera
    return a,b

with open('liczby1.txt','r') as ff:
    result = 0
    for line in ff:
        divisor = math.gcd(funkcja(int(line))[0], funkcja(int(line))[1])
        if divisor == 1:
            result += 1
print(result)