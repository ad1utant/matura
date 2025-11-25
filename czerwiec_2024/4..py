#4.2.
# secik, secik_all, counter = set(), set(), 0
# with open('odbiorcy.txt','r') as ff:
#     for line in ff:
#         secik.add(int(line.strip()))
#         counter += 1
#         secik_all.add(counter)
# print(len(secik_all - secik))
from copy import deepcopy

#4.3
counter, runda = 1, 1
dictionary_ref, dictionary_temp, dictionary_current = dict(), dict(), dict()
with open('odbiorcy_przyklad.txt','r') as ff:
    for line in ff:
        dictionary_ref[counter] = int(line.strip())
        dictionary_current[counter] = int(line.strip())
        dictionary_temp[counter] = int(line.strip())
        counter += 1
    for i in range(1):
        for key,value in dictionary_ref.items():
            dictionary_temp[value] = dictionary_current[key]

        print(runda)
        # print(dictionary_ref)
        # print(dictionary_temp)
        print(dictionary_current)
        print()
        dictionary_current = deepcopy(dictionary_temp)
        print(dictionary_current)
        for key, value in dictionary_current.items():
            if key == value:
                print(runda, value, key)
        runda += 1