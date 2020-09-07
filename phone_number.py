def create_phone_number(n):
    x = [str(n[i])for i in range(len(n))]
    x.insert(0, "(")
    x.insert(4, ")")
    x.insert(8, "-")
    x.insert(9, " ")
    print(x)
    y = "".join(x)
    print(y)




n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#Desired output: "(123) 456-7890"






n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(n))

# Desired output: "(123) 456-7890"