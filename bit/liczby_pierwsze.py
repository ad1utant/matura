import math
from itertools import count
from zoneinfo import reset_tzpath

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def how_many_primes(n):
    count = 0
    if n == 1:
        return 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count

def list_of_primes(n):
    if n == 1:
        return 0
    return [i for i in range(2,n) if is_prime(i)]

def list_of_prime_factors(n):
    tab = []
    for i in range(2, n):
        if n == 1:
            return tab
        while n % i == 0:
            n = n // i
            tab.append(i)
    return tab

def unique_prime_factors(n):
    return set(list_of_prime_factors(n))

print(unique_prime_factors(420))

