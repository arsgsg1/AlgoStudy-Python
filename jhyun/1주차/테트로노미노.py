N, M = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(N)]
blocks = [
    [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    [[1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]],
    [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]],
    [[1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
]
table = [[0] * (M + 6) for _ in range(N + 6)]
for i in range(N):
    for j in range(M):
        table[i + 3][j + 3] = arr[i][j]
#input end
def rotate_2d_list_clock(arr: list) -> list:
    row_len = len(arr)
    col_len = len(arr[0])
    temp = [[0] * row_len for _ in range(col_len)]
    for c in range(col_len):
        for r in range(row_len):
            temp[c][row_len - r - 1] = arr[r][c]
    return temp
def rotate(arr: list, degree: int):
    temp = arr.copy()
    while degree:
        degree -= 1
        temp = rotate_2d_list_clock(temp)
    return temp
def symmetry(arr: list):
    temp = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            temp[i][4 - j - 1] = arr[i][j]
    return temp
def get_point(r: int, c: int, block: list):
    point = 0
    for i in range(4):
        for j in range(4):
            point += table[r + i][c + j] * block[i][j]
    return point
def solve():
    res = 0
    for i in range(len(table) - 3):
        for j in range(len(table[0]) - 3):
            for block in blocks:
                for k in range(4):
                    temp = rotate(block, k)
                    res = max(res, get_point(i, j, temp))
                    res = max(res, get_point(i, j, symmetry(temp)))
    return res
#main
print(solve())