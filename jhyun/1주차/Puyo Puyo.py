# 37m
from collections import deque
arr = [
    [x for x in input()] for _ in range(12)
]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def in_range(r: int, c: int) -> bool:
    return 0 <= r < 12 and 0 <= c < 6
def bfs(row: int, col: int, visit: list) -> list:
    q = deque([(row, col)])
    cnt, color = 1, arr[row][col]
    booms = []
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if not in_range(nr, nc): continue
            if not visit[nr][nc] and arr[nr][nc] == color:
                booms.append((nr, nc))
                visit[nr][nc] = True
                cnt += 1
                q.append((nr, nc))
    return booms
def gravity():
    global arr
    for c in range(6):
        q = deque([])
        for r in range(11, -1, -1):
            if arr[r][c] != '.':
                q.append((arr[r][c]))
        for r in range(11, -1, -1):
            if len(q):
                arr[r][c] = q.popleft()
            else:
                arr[r][c] = '.'
def solve():
    answer = 0
    while True:
        is_boom = False
        gravity()
        visit = [[False] * 6 for _ in range(12)]
        for r in range(12):
            for c in range(6):
                if arr[r][c] != '.':
                    booms = bfs(r, c, visit)
                    if len(booms) >= 4:
                        is_boom = True
                        while len(booms):
                            cur_r, cur_c = booms.pop()
                            arr[cur_r][cur_c] = '.'
        if is_boom:
            answer += 1
        else:
            break
    print(answer)
solve()