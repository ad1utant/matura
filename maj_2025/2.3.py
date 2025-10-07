dd = []
symbols = []
with (open('symbole.txt') as ff):
    for line in ff:
        strip_line = line.strip()
        symbols.append(strip_line)
        strip_line = strip_line.replace('o', '0').replace('+', '1').replace('*', '2')
        dd.append(int(strip_line, 3))
    print(max(dd))

print(symbols[dd.index(max(dd))])