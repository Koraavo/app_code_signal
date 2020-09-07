def allLongestStrings(inputArray):
    list1 = []
    list3 = []

    for i in range(len(inputArray)):
        list1.append(len(inputArray[i]))
    maxi = max(list1)
    print(maxi)

    for i in range(len(inputArray)):
        if len(inputArray[i]) == maxi:
            list3.append(inputArray[i])
    print(list3)


inputArray = ["abc", "eeee", "abcd", "dcd"]
# inputArray = ["aba", "aa", "ad", "vcd", "aba"]
allLongestStrings(inputArray)

