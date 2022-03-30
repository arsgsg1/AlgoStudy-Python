from collections import deque

data = list(input().split("\n"))
t = int(data[0])
r,c = map(int,data[1].split())
d =[list(map(int,data[i])) for i in range(r)]
descr =[list(map(int,data[i].split())) for i in range(r,2*r)]



##bfs로 푼다
## 큐에서 꺼내기 -> 인접한것 찾기 -> 인접한것이 그 조합안에 있는지 + 주변에 다른같은 숫자 있는지 탐색
##-> 큐에 포함시키기 -> 큐 끝날떄 까지 반복 -> visited에 넣기

def search_connected(x,y):
    connected = []#연결된 점
    temp = descr[x][y]
    if temp % 2 != 0 :  #홀수라면
        connected.append((x-1,y))
        temp -= 1
    if temp >= 8 :
        connected.append((x,y-1))
        temp -= 8
    if temp >= 4 :
        connected.append((x+1,y))
        temp -= 4
    if temp >= 2 :
        connected.append((x,y+1))
        temp -= 2
    return connected



dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    global visited
    grid =[] #(x,y)와 연결된 노드들
    grid.append(d[x][y])
    temp =[] #방문 여부
    temp.append((x,y))
    q = deque()
    q.append((x,y))
    while q :
        x,y = q.popleft()
        connected = search_connected(x,y)

        if connected == [] : #연결된 곳이 없다면
            visited.append((x,y))
            return
        for nx,ny in connected : #큐에서 꺼낸 x,y와 인접한 노드

            if (nx,ny) in temp : continue # 이미 탐색한 것은 건너 뜀

            #탐색(인접한 블럭이 격자 안에 있는지)
            if nx <0 or nx >= r or ny <0 or ny >= c : return False

            #탐색(주변에 동일한 숫자가 있는지)
            num = d[nx][ny]
            for i in range(1,num+1):
                for j in range(4):
                    sx = nx + dx[j] * i
                    sy = ny + dy[j] * i
                    if sx < 0 or sx >= r or sy < 0 or sy >= c: continue
                    if d[sx][sy] == num:  # 동일한 숫자가 주변에 있다면
                        print(3)
                        return False

            #탐색(그리드 안에 동일한 숫자가 있는 지)
            if d[nx][ny] in grid : return False

            #탐색(이미 다른 그리드에 속해 있는지)
            if (nx,ny) in visited :
                return False


            grid.append(d[nx][ny]) #그리드에 숫자
            temp.append((nx,ny)) #방문
            q.append((nx,ny)) #인접 노드 추가

    visited += temp #그리드에 포함된 것을 방문처리
    return True


def solution() :
    visited = []
    for i in range(r):
        for j in range(c) :
            if d[i][j] == 1 :
                if bfs(i,j) == False :
                    print("invalid")
                    return
    print("valid")


#데이터 받아들이기
t = int(input())
for i in range(t) :
    r,c = map(int,input().split())
    d = [list(map(int,input()))for _ in range(r)]
    descr = [list(map(int,input().split())) for _ in range(r)]
    solution()


