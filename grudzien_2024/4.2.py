with open('prostokaty_przyklad.txt', 'r', encoding='utf8') as ff:
    tab = [list(map(int, row.split())) for row in ff]
print(tab)

strike = []
count = 1
for i in range(1, len(tab)):
    xp, yp = tab[i-1][0], tab[i-1][1]
    x,y = tab[i][0], tab[i][1]
    if xp >= x and yp >= y:
        count += 1
    else:
        strike.append([count, xp, yp])
        count = 1

m = max(strike)
print(m)