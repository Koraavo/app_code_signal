def commonCharacterCount(s1, s2):
    list3 = []
    list1 = list(s1)
    list2 = list(s2)
    print(list1)
    print(list2)

    for char in list1:
        if char in list2:
            list3.append(char)
            x = list2.index(char)
            list2.pop(x)
    print(list3)
    print(len(list3))


# s1 = "abca"
# s2 = "xyzbac"

# s1 = "zzzz"
# s2 = "zzzzzzz"

s1 = "aabcc"
s2 = "adcaa"

print(commonCharacterCount(s1, s2))