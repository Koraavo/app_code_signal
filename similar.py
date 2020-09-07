def areSimilar(a, b):
    list1 = [[a[i], b[i]] for i in range(len(a)) if a[i] != b[i]]
    if len(list1) < 2:
        return True
    if len(list1) > 2:
        return False
    else:
        if list1[0][0] == list1[1][1] and list1[0][1] == list1[1][0]:
            return True
        else:
            return False


a = [832, 998, 148]
b = [832, 998, 148]
print(areSimilar(a, b))


def areSimilar(a, b):
    return sorted(a) == sorted(b) and sum(i != j for i, j in zip(a, b)) < 3


from collections import Counter as C


def areSimilar(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3
