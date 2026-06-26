list = [1,3,5,7,2,4,54]

k = list[0]

for i in range(len(list)):
    for j in range(len(list)):
        if list[i] < list[j]:
            k = list[i]
            list[i] = list[j]
            list[j] = k

for i in range(len(list)):
    print(list[i])

#to je bubble sort algo s pomočjo katerega sortiramo, je ez način za prikaz nested loopov