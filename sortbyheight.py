def sortByHeight(a):
    list1 = []
    index_var = 0
    x = sorted(a)
    list1 = [x[i] for i in range(len(x))if x[i] != -1]

    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i] = list1[index_var]
            index_var += 1
    print(a)

a = [-1, 150, 190, 170, -1, -1, 160, 180]

sortByHeight(a)

####
## OR

def sortByHeight(a):
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            for j in range(len(a)):
                if a[i] < a[j]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
    print(a)

a = [-1, 150, 190, 170, -1, -1, 160, 180]

sortByHeight(a)
