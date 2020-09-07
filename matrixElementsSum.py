def matrixElementsSum(matrix):
    # create a vertical matrix in a 4x3 mode(rows become columns and columns become rows)
    # add all the elements before 0 in each row
    vertical_matrix = []
    for i in range(len(matrix[0])):
        x = [item[i] for item in matrix]
        vertical_matrix.append(x)
    # [[0, 0, 2], [1, 5, 0], [1, 0, 3], [2, 0, 3]]


    new_list = []
    # if [0,1] == 0, break and change i to 1, then to 2 and 3
    # else continue to append in new list with increase of j[0,1,2]
    for i in range(len(vertical_matrix)):
        for x in range(len(vertical_matrix[i])):
            if vertical_matrix[i][x] == 0:
                break
            else:
                new_list.append(vertical_matrix[i][x])
    print(new_list)
    print(sum(new_list))


matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

matrixElementsSum(matrix)