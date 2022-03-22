# puyo puyo
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, flag):
    q = deque()
    c = [[0]*6 for _ in range(12)]
    q.append([x, y])
    cnt = 1
    c[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if a[nx][ny] == a[x][y] and c[nx][ny] == 0:
                    cnt += 1
                    c[nx][ny] = 1
                    q.append([nx, ny])

    if cnt >= 4:
        flag += 1
        for i in range(12):
            for j in range(6):
                if c[i][j] == 1:
                    a[i][j] = '.'
    return flag

def check_fall():
    for i in range(10, -1, -1):
        for j in range(6):
            if a[i][j] != '.' and a[i+1][j] == '.':
                for k in range(i+1, 12):
                    if k == 11 and a[k][j] == '.':
                        a[k][j] = a[i][j]
                    elif a[k][j] != '.':
                        a[k-1][j] = a[i][j]
                        break
                a[i][j] = '.'

a = [list(map(str, input().strip())) for _ in range(12)]

ans = 0
while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if a[i][j] != '.':
                cnt = bfs(i, j, cnt)
    if cnt == 0:
        print(ans)
        break
    else:
        ans += 1
    check_fall()