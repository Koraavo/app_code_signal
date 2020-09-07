a = [-1, 150, 190, 170, -1, -1, 160, 180]
b = [-1, 150, 190, 170, -1, -1, 160, 180]
for i in range(len(a)):
    for j in range(len(a)):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        print(f"i = {i}, j = {j}, temp: {temp}, a[i]: {a[i]}, a[j]: {a[j]}")
    print("")

# x = [1,2,3,4]
# y = [5,6,7,8]
# for c in range(len(x)):
#     for d in range(len(y)):
#         temp = x[c]
#         x[c] = y[d]
#         y[d] = temp
#         print(f"c: {c}, d: {d}, temp: {temp}, x[c]: {x[c]}, y[d]: {y[d]}")
#     print("")

