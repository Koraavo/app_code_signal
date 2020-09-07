def addBorder(picture):

    # amount of rows and columns to enclose the picture
    rows = len(picture) + 2
    columns = len(picture[0])+2
    output = []
    border = ""
    for i in range(columns):
        border += "*"
    output.append(border)
    for i in range(len(picture)):
        output.append("*" + picture[i] + "*")
    output.append(border)
    print(output)

    # or
    l = len(picture[0]) + 2
    return ["*" * l] + [x.center(l, "*") for x in picture] + ["*" * l]


picture = ["abc",
           "ded"]

print(addBorder(picture))
