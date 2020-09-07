def alternatingSums(a):
    # list1, list2 = [a[i] for i in range(len(a)) if i % 2 == 0], [a[i] for i in range(len(a)) if i % 2 != 0]
    # return [sum(list1), sum(list2)]

    # or
    return [sum(a[::2]), sum(a[1::2])]


a = [50, 60, 60, 45, 70]
alternatingSums(a)