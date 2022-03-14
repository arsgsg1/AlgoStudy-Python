import sys
input = sys.stdin.readline
R, C = map(int, input().split())
arr = [[x for x in input().rstrip()] for _ in range(R)]
visit = [[False] * C for _ in range(R)]
dirs = [(-1, 1), (0, 1), (1, 1)]

def in_range(r: int, c: int) -> bool:
    return 0 <= r < R and 0 <= c < C

def can_visit(r: int, c: int) -> bool:
    if arr[r][c] == 'x': return False
    if visit[r][c]: return False
    return True

def dfs(r: int, c: int) -> bool:
    if c == C - 1:
        return True

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc): continue
        elif not can_visit(nr, nc): continue
        visit[nr][nc] = True
        if dfs(nr, nc): #파이프를 연결했다면 다음 파이프를 연결하지 않도록 함
            return True
    return False

ans = 0
for i in range(0, R):
    if dfs(i, 0):
        ans += 1
print(ans)