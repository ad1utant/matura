global_level, global_great_number = 0,0
def cut(inp):
    global global_level, global_great_number
    sqr = str(inp*inp)
    length = len(sqr)
    local_level = 0
    for i in range(length - 1):
        a = int(sqr[:i+1])
        b = int(sqr[i+1:])
        if a+b <= inp:
            local_level += 1
    if local_level > global_level:
        global_level = local_level
        global_great_number = inp
    return global_level
with open('liczby2.txt', 'r') as ff:
    for line in ff:
        global_level = cut(int(line))
print(global_level, global_great_number)