tab = []
def ln(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

def to_bin(n):
    p = 1
    s = 0
    while n > 0:
        k = n % 2
        n //=2
        s += k * p
        p *= 10
    return s

def zad1(n,k,w):
    binary = to_bin(n)
    bin_len = ln(binary)
    fields = k * w
    while fields > 0:
        fields -= bin_len
    fields *= -1
    while fields > 0:
        binary //= 10
        fields -= 1
    return binary % 10

print(zad1(42,10,1))