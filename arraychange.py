# def arrayChange(inputArray):
#     counter = 0
#     for i in range(len(inputArray)-1):
#         while inputArray[i] >= inputArray[i+1]:
#             inputArray[i+1] = inputArray[i+1]+1
#             counter += 1
#     return counter
#
#
# inputArray = [3122, -645, 2616, 13213, -8069]
# print(arrayChange(inputArray))

def arrayChange(inputArray):
    counter = 0
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            counter += inputArray[i]-inputArray[i+1]+1
            inputArray[i+1]=inputArray[i]+1
    return counter


inputArray = [3122, -645, 2616, 13213, -8069]
print(arrayChange(inputArray))
print(inputArray)