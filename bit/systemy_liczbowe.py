def decimal_to_any(f_sys ,d_sys : int, number: int):
    temp = int(number, f_sys)
    new = ''
    while temp > 0:
        to_string = temp % d_sys
        temp = temp // d_sys
        new += str(to_string)
    return int(new[::-1])

print(decimal_to_any(2,10, 283))
