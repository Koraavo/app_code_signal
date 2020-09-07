def isLucky(n):
    number = str(n)
    list1 = [int(number[i]) for i in range(len(number) //2)]
    list2 = [int(number[i]) for i in range(len(number) // 2, len(number))]

    if sum(list1) == sum(list2):
        return True
    return False
n = 1230
print(isLucky(n))