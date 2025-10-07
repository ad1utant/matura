def skroc(x):
    x = str(x)
    if len(x) == 1:
        return 0
    return int(x[:-1])
def dopisz(x):
    x = str(x)
    if x == '0':
        return int(x)
    return int(x+'0')
def ostatnia(x):
    x = str(x)
    return int(x[-1])

count = 0
def funkcja(a, b):
    global count
    if b == 0:
        return 0
    k = ostatnia(b)
    w = funkcja(a, skroc(b))
    w = dopisz(w)
    while k > 0:
        w = w + a
        count += 1
        k = k - 1
    return w

print(funkcja(2024,1234,),count)