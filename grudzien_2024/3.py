with open('liczby.txt', 'r', encoding='utf8') as ff:
    tab = [int(c) for c in ff]

new_tab = []
for i in tab:
    if int(i ** (1/2)) == i ** (1/2):
        new_tab.append(i)
print(len(new_tab), print(new_tab[0]))