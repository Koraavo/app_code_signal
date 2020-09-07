# https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN

# def centuryFromYear(year):
#     century = ((year-1) // 100) + 1
#     return century
#
# print(centuryFromYear(2000))

# def adjacentElementsProduct(inputArray):
#     list1 = []
#     for i in range(len(inputArray)):
#         if i > len(inputArray) - 2:
#             break
#         else:
#             mul = inputArray[i]*inputArray[i+1]
#             list1.append(mul)
#     print(max(list1))


# def adjacentElementsProduct(inputArray):
#     # print(inputArray[i] for i in range(len(inputArray)))
#     print(max(inputArray[i]*inputArray[i+1] for i in range(len(inputArray)-1)))
#
# adjacentElementsProduct([1, 3, 4, 7, 8])
#
#
# def shapeArea(n):
#     return (n**2) + (n-1)**2
#
# print(shapeArea(3))
#
# def makeArrayConsecutive2(statues):
#     lista = (list(i for i in range(min(statues), max(statues)) if not i in statues))
#     print(len(lista))
#
# makeArrayConsecutive2([6, 2, 3, 8])
