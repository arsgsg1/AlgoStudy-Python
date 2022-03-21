# 상어 초등학교

import sys
count = 0
def solve(i,j):
    global count
    count+=1
    if j == c-1:
        return True
    for d in dx:
        if 0<=i+d<r and grid[i+d][j+1]=="." and not visit[i+d][j+1]:
            visit[i+d][j+1] = True
            if solve(i+d, j+1):
                return True
    return False

r, c = map(int, sys.stdin.readline().rstrip("\n").split())
grid = []
visit = [[False]*c for _ in range(0,r)]
for i in range(0,r):
    grid.append(list(sys.stdin.readline().rstrip("\n")))
dx = [-1,0,1]
ans = 0
for i in range(0,r):
    if grid[i][0] == ".":
        if solve(i,0):
            ans+=1

print(ans)