NumList = [-1, 150, 190, 170, -1, -1, 160, 180]
Number = 8
for i in range (Number):
    for j in range(i + 1, Number):
        if(NumList[i] > NumList[j]): # num[0] > num[1]
            temp = NumList[i] # temp = num[0] = 5
            NumList[i] = NumList[j] # num[0] = 10 # lst = [5,10,15,20]
            NumList[j] = temp # [5, 5, 15, 20] # right?
            print(temp, NumList[i], NumList[j])

print(NumList)