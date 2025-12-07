#zadanie 1
def convert_to_decimal(n, p):
    result = 0
    for i in range(len(str(n))-1, -1, -1):
        result += p**i * int(str(n)[len(str(n)) - 1 - i])
    return result

def add_numbers(x : int,y : int,p : int) -> int:
    return convert_to_decimal(x, p) + convert_to_decimal(y, p)

print(add_numbers(74563, 6477, 8))

#zadanie 2
def unique_prime_factors_sum(n):
    tab = []
    for i in range(2, n):
        if n == 1:
            break
        while n % i == 0:
            n = n // i
            tab.append(i)
    f_sum = 0
    for i in set(tab):
        f_sum += i
    return f_sum

def if_sum_greater(n):
    sum_of_digits = 0
    for i in str(n):
        sum_of_digits += int(i)
    sum_of_unique_primes = unique_prime_factors_sum(n)
    return True if sum_of_digits > sum_of_unique_primes else False

print(if_sum_greater(77))