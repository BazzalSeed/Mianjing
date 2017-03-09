
def countSquare(self, hor, ver):

    result = 0

    hor_m, hor_n = len(hor), len(hor[0])
    ver_m, ver_n = len(ver), len(ver[0])
    DP_Hor = [[0 for x in range(hor_m)] for y in range(len(hor_n))]
    DP_Ver = [[0 for x in range(ver_n)] for y in range(ver_m)]

    for i in range(hor_m):
        for j in range(hor_n):
            if hor[i][j] == 1:
                DP_Hor[i][j] = 1 if j == 0 else DP_Hor[i][j - 1] + 1
            else:
                DP_Hor[i][j] = 0

    for i in range(ver_m):
        for j in range(ver_n):
            if ver[i][j] == 1:
                DP_Ver[i][j] = 1 if j == 0 else DP_Ver[i][j - 1] + 1
            else:
                DP_Ver[i][j] = 0

    for i in range(hor_m):
        for j in range(hor_n):
            for l in range(1, min(hor_n - i, ver_n - j)):
                if DP_Hor[i][j + l - 1] >= l and DP_Hor[i + l][j + l - 1] >= l and DP_Ver[j][i + l - 1] >= l and DP_Ver[j + l][i + l - 1] >= l:
                    result += 1

    return result
