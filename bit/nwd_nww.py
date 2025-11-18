from collections import Counter


def prime_factors(n):
    i, list_of_primes = 2, []
    if n == 1:
        return []
    while n > 1:
        if n % i == 0:
            n //= i
            list_of_primes.append(i)
        else:
            i += 1
    return list_of_primes


def nwd(a, b):
    a_primes, b_primes = prime_factors(a), prime_factors(b)
    Counter(a_primes)
    ca = Counter(a_primes)
    cb = Counter(b_primes)
    common = cb & ca
    mul = 1
    print(common)
    for i in common.elements():
        print(i)
        mul *= i
    return mul


def nww(a, b):
    a_primes, b_primes = prime_factors(a), prime_factors(b)
    Counter(a_primes)
    return set(a_primes).union(set(b_primes))

print(nww(4,6))

def convert_to_decimal(n, p):
    result = 0
    for i in range(len(str(n))-1, -1, -1):
        result += p**i * int(str(n)[len(str(n)) - 1 - i])
    return result


#zadanie szkopul
def zadanie(n, p):
    x = convert_to_decimal(n,p)
    if len(prime_factors(x)) == 1:
        return True
    return False

def convert_to_decimal_2nd_vers(n, p):
    result = 0
    i = len(str(n)) - 1
    for j in str(n)[::-1]:
        result += p**i * int(j)
        i -= 1
    return result