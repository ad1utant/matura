numbers = {'0','1','2','3','4','5','6','7','8','9'}
dictionary = dict(
    {'0':0,
     '1':0,
     '2':0,
     '3':0,
     '4':0,
     '5':0,
     '6':0,
     '7':0,
     '8':0,
     '9':0}
)


result = 0
with open('dane.txt', 'r') as ff:

    for line in ff:
        for i in range(1, len(line.strip()) - 1):
            if line[i] in numbers:
                dictionary[line[i]] += 1


print(result,dictionary)