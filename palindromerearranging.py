def palindromeRearranging(inputString):
    odds=0
    myset=set(inputString)
    print(myset)
    for i in myset:
        n=inputString.count(i)
        if n%2!=0:
            odds+=1
    print(odds)
    return odds <= 1

#   OR
#     return sum([inpustString.count(i)%2 for i in set(inputString)]) <= 1

inputString = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccaaaaaaaaaaaaa'
print(palindromeRearranging(inputString))