def funkcja(k):
    pom = k
    length = 0
    zera = 1
    while True:
        k//= 10
        length+=1
        if k == 0:
            break
    print(length,zera)
    for j in range(length//2):
        zera *= 10
    print(length, zera)
    a = pom//zera
    b = pom%zera
    return a,b
print(funkcja(112342345534))