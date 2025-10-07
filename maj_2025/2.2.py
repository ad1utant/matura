tab, count = [], 0

with (open('symbole.txt') as ff):
    for line in ff:
        strip_line = line.strip()
        x = []
        for sign in strip_line:
            x.append(sign)
        tab.append(x)

for i in range(1, len(tab) - 1):
    for j in range(1, len(tab[i]) - 1):
        middle_sign = tab[i][j]
        if tab[i-1][j-1] == middle_sign and tab[i+1][j+1] == middle_sign \
                and tab[i][j-1] == middle_sign and tab[i-1][j] == middle_sign \
                and tab[i][j+1] == middle_sign and tab[i+1][j] == middle_sign \
                and tab[i+1][j-1] == middle_sign and tab[i-1][j+1] == middle_sign:
            count += 1
            print(i+1, j+1)

print(count)