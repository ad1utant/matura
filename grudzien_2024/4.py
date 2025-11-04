areas = []

with open('prostokaty_przyklad.txt', 'r', encoding='utf8') as ff:
    tab = [list(map(int, row.split())) for row in ff]
print(tab)

for i in tab:
    areas.append(i[0]*i[1])
print(max(areas), min(areas))