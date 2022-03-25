##로직
-bfs 유형으로 품
-빨간공과 파란공을 동시에 움직이되 만약 두 공의 위치가 같다면 두 공 중 움직인 거리가 긴 공을 한칸 전으로 되돌려줌
-이동할 위치 탐색 -> 이동하게 될 위치의 예외 판단 -> 이동 + 횟수 증가

##쟁점
- 많은 예외상황을 어떻게 처리할 것인지
 => 이동하게 된 두 공의 위치가 같다면 더 길게 움직인 공의 위치를 한 칸 뒤로 조정
 => 큐에 이동횟수 count를 포함시켜 이동한 횟수를 추가하면서 반복

##배운점
- bfs사용 시 이동할 위치 탐색 -> 이동하게 될 위치의 예외 판단 -> 이동 순으로 깔끔하게 정리할 수 있음
- 탐색문제에서 방문한 노드 정보를 꼭 2차원 리스트로 할 필요 없이 1차원 리스트에 방문한 좌표를 append하는 방식으로 처리할 수 있음

from collections import deque
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

# 빨간공 파란공 위치 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            red = (i,j)
        elif graph[i][j] == "B":
            blue = (i,j)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x1,y1,x2,y2) : #레드와 블루의 위치
    q = deque()
    q.append((x1,y1,x2,y2,0))  #몇번 움직였는지도 꼭 체크해줌
    visited = []
    visited.append((x1,y1,x2,y2)) #방문처리
    while q :
        x1, y1, x2, y2,count = q.popleft()
        # 10번넘어가면 초과
        if count > 10:
            print(-1)
            return
        # 끝내는 상황/ 블루가 먼저 홀에 들어가는 예외상황은 이동 전에 체크해서 미리 제거시켜줌
        if graph[x1][y1] == "O":
            print(count)
            return
        # 이동탐색
        for i in range(4):
            # 빨간색 공 먼저 이동
            nx1, ny1 = x1, y1
            while True:  # 벽이나 구멍때 까지
                nx1 += dx[i]
                ny1 += dy[i]
                if graph[nx1][ny1] == "#":  # 만약 벽이면 한칸 전으로 옮겨서 위치 고정
                    nx1 -= dx[i]
                    ny1 -= dy[i]
                    break
                if graph[nx1][ny1] == "O":  # 만약 구멍이었으면 그냥 끝
                    break
            # 파란색 공 이동
            nx2, ny2 = x2, y2
            while True:
                nx2 += dx[i]
                ny2 += dy[i]
                if graph[nx2][ny2] == "#":
                    nx2 -= dx[i]
                    ny2 -= dy[i]
                    break
                if graph[nx2][ny2] == "O":
                    break

            # 예외상황
            if graph[nx2][ny2] == "O":  # 블루가 먼저 들어갈 경우
                continue  # 한턴 넘김

            # 위치 체크
            if nx1 == nx2 and ny1 == ny2:
                if abs(nx1 - x1) + abs(ny1 - y1) > abs(nx2 - x2) + abs(ny2 - y2):  # 양쪽 중 많이 움직인 쪽이 있다면
                    nx1 -= dx[i]
                    ny1 -= dy[i]  # 한칸 뒤로 뻄
                else:
                    nx2 -= dx[i]
                    ny2 -= dy[i]  # 한칸 뒤로 뻄

            # 이동
            if (nx1, ny1, nx2, ny2) not in visited:  # 방문한적 없는 곳이라면
                q.append((nx1, ny1, nx2, ny2, count+1))  # 큐에 넣고
                visited.append((nx1, ny1, nx2, ny2))  # 방문처리
    print(-1)
    return


bfs(red[0],red[1],blue[0],blue[1])


