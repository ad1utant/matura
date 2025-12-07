count = 0

def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -=1
    return fact

with open('liczby.txt','r') as ff:
    for line in ff:
        fact_sum = 0
        for sign in line.strip():
            fact_sum += factorial(int(sign))
        print(fact_sum) if int(line.strip()) == fact_sum else print('',end='')