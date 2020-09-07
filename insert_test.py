def insert1(pos):
    list1 = [n[i] for i in range(pos)]
    return list1

def insert3(pos):
    list2 = [n[i] for i in range(pos+1, len(n))]
    return list2

def insert2(pos, elements):
    old_number = [n[pos]]
    n[pos] = [elements]
    n[pos].extend(old_number)
    return n[pos]

def insert4(pos, elements):
    part1 = insert1(pos)
    part2 = insert2(pos, elements)
    part3 = insert3(pos)
    return part1+part2+part3


n = [8, 9, 9, 1, 5, 4, 3, 6, 2, 1]
# print(insert1(0))
print(insert4(0, "**"))
print(insert4(2, "**"))
print(insert4(5, "****"))
# ['XX', 8, 'XXXX', 9, 9, 'XXXXX', 1, 5, 4, 3, 6, 2, 1]