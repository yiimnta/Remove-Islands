def removeIsLands(matrix):
    if matrix is []:
        return []

    length = len(matrix)

    if length <= 2:
        return matrix

    # create a matrix[length][length] to contain the valid pixels (be connected with the black-pixels in border)
    rs = [[False] * length for i in range(length)]

    # mark all positions of the black-pixels at the border ( if found set the value of the position is TRUE)
    for i in range(0, length):
        if matrix[0][i] == 1:
            rs[0][i] = True
        if matrix[i][0] == 1:
            rs[i][0] = True
        if matrix[i][length - 1] == 1:
            rs[i][length - 1] = True
        if matrix[length - 1][i] == 1:
            rs[length - 1][i] = True

    # read each stage (max stage = int(length / 2)) from border to center to find the connection between black pixels
    for i in range(1, int(length / 2)):

        # at each stage, we will find the connection of black pixels
        for j in range(i, length - i - 1):
            if matrix[i][j] == 1:
                if rs[i - 1][j] or rs[i][j - 1] or rs[i + 1][j] or rs[i][j + 1]:
                    rs[i][j] = True
            if matrix[j][i] == 1:
                if rs[j - 1][i] or rs[j][i - 1] or rs[j + 1][i] or rs[j][i + 1]:
                    rs[j][i] = True
            if matrix[j][length - 1 - i] == 1:
                if rs[j - 1][length - 1 - i] or rs[j][length - i - 2] or rs[j + 1][length - 1 - i] or rs[j][
                    length - 1 - i + 1]:
                    rs[j][length - i - 1] = True
            if matrix[length - i - 1][j] == 1:
                if rs[length - i - 2][j] or rs[length - i - 1][j - 1] or rs[length - i][j] or rs[length - i - 1][j + 1]:
                    rs[length - i - 1][j] = True

    # with each True value, it will be converted to 1
    for i in range(0, length):
        for j in range(0, length):
            if rs[i][j]:
                rs[i][j] = 1
            else:
                rs[i][j] = 0

    # print to check result
    for i in range(length):
        print(rs[i])

    return rs


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]

removeIsLands(matrix=matrix)
