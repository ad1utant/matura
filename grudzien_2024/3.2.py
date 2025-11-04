def prime_factors(n):
    prime_factors_tab = []
    for d in range(2, n + 1):
        if n == 1:
            return set(prime_factors_tab)
        while n % d == 0:
            n //= d
            prime_factors_tab.append(d)
    return set(prime_factors_tab)

with open('liczby.txt', 'r', encoding='utf8') as ff:
    tab = [int(c) for c in ff]

for i in tab:
    if len(prime_factors(i)) >= 5:
        print(i)