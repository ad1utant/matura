count = 0

def is_power_of_three(n):
    powered_num = 1
    power = 0
    while n > powered_num:
        power += 1
        powered_num *= 3
    if powered_num == n:
        return (True, n)
    else:
        return (False, n)

with open('liczby.txt','r') as ff:
    for line in ff:
        n = int(line.strip())
        if is_power_of_three(n)[0]:
            print(is_power_of_three(n)[1])
            count += 1
print(f'{count=}')
