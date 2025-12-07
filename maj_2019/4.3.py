def nwd(a,b):
    if a > b:
        a,b = a,b
    else:
        a,b = b,a
    rest = 0
    while a % b != 0:
        rest = a % b
        a = b
        b = rest
    return b

tab,lista = [],[]
with open('liczby.txt','r') as ff:
    for line in ff:
       tab.append(int(line.strip()))

for i in range(len(tab)):
    j = 1
    general_nwd = tab[i]
    while True:
        try:
            new_nwd = nwd(general_nwd,tab[i+j])
        except IndexError:
            lista.append((tab[i], j))
            break
        if new_nwd > 1:
            j += 1
            general_nwd = new_nwd
        else:
            lista.append((tab[i],j, general_nwd))
            break
print(max(lista, key=lambda x:x[1]))