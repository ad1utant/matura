with open('symbole.txt') as ff:
    for line in ff:
        x = line.strip()
        if x == x[::-1]:
            print(x)