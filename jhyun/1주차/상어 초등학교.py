import heapq as hq
from collections import defaultdict
N = int(input())
arr = [[0] * N for _ in range(N)]
wait, pq = [], []
board = defaultdict(list)
def get_point() -> int:
    result = 0
    for r in range(N):
        for c in range(N):
            like = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                cur = arr[r][c]
                if not in_range(nr, nc): continue
                if arr[nr][nc] in board[cur]:
                    like += 1
            if like != 0:
                result += 10 ** (like - 1)
    return result
def in_range(r: int, c: int):
    return 0 <= r < N and 0 <= c < N
for _ in range(N ** 2):
    num, a1, a2, a3, a4 = map(int, input().split())
    board[num] = [a1, a2, a3, a4]
    wait.append(num)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for cur in wait:
    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0: continue
            empty, like = 0, 0
            for dr, dc in dirs: # 빈칸 개수
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc): continue
                if arr[nr][nc] == 0:
                    empty += 1
            for dr, dc in dirs: # 좋아하는 학생 수
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc): continue
                if arr[nr][nc] != 0 and arr[nr][nc] in board[cur]:
                    like += 1
            hq.heappush(pq, (-like, -empty, r, c))
    like, empty, r, c = hq.heappop(pq)
    arr[r][c] = cur
    pq = []
answer = get_point()
print(answer)