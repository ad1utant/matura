with open('liczby.txt', 'r', encoding='utf8') as ff:
    tab = [int(c) for c in ff]
less, more, equal = 0, 0, 0
for line in tab:
    M = int(''.join(sorted(str(line), reverse = True)))
    m = int(''.join(sorted(str(line))))
    if M - m > line:
        more += 1
    elif M - m < line:
        less += 1
    elif M - m == line:
        print(line)
        equal += 1
print(f'{equal = }, {less = }, {more = }')