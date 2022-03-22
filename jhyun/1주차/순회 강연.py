import heapq as hq
N = int(input())
q, visit = [], [False] * 10001
answer = 0
for _ in range(N):
    p, d = map(int, input().split())
    hq.heappush(q, (-p, d))
while q:
    p, d = hq.heappop(q)
    p *= -1
    for idx in range(d, 0, -1):
        if not visit[idx]:
            answer += p
            visit[idx] = True
            break
print(answer)