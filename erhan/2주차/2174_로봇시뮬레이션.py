##로직
- 이동위치 탐색 -> 문제 체크 -> 이동 -> 위치 갱신

##쟁점
-좌표계가 다름
 => 2차원 리스트 안만들고 구현

##틀린이유
틀렸습니다.

data = input().split("\n")
A,B = map(int,data[0].split())
n,m = map(int,data[1].split())
robot= []
for i in range(2,n+2):
    x,y,d = data[i].split()
    direc = ["N", "E", "S", "W"]
    robot.append((int(x) - 1, int(y) - 1, direc.index(d)))
order = []
for j in range(n+2,n+m+2):
    idx, turn, move = data[j].split()
    order.append((int(idx) - 1, turn, int(move)))


#방향 정의
dx = [0,1,0,-1]
dy = [1,0,-1,0]

#초기 로봇 위치
space ={}
for i in range(n):
    x,y,d = robot[i]
    space[(x,y)] = i


##방향탐색
def check_direc(d,turn):
    if turn == "R" :
        d = (d +1 ) % 4
    elif turn == "L":
        d = (d + 3)%4
    else :
        d = d
    return d

## 이동 및 이동가능탐지
def move_robot(info): #input : 명령 하나
    idx,turn,move = info
    #로봇 현재위치
    x,y,d = robot[idx]

    #이동 위치 탐색
    d = check_direc(d,turn)
    for i in range(1,move+1) :
        nx,ny = x + i * dx[d], y + i * dy[d]
        if nx < 0 or nx >= A or ny <0 or ny >= B : #격자 밖
            return [idx+1]
        elif (nx,ny) in space : #로봇 충돌
            return [idx+1,space[(nx,ny)] + 1 ]

    nx,ny = x + move *dx[d] , y + move*dy[d]

    #위치 갱신 #space갱신필요, robot갱신필요
    del space[(x,y)] # 기존 위치 삭제
    space[(nx,ny)] = i #새로운 위치 추가

    robot[idx] = (nx,ny,d) #위치 및 방향 갱신
    return []


temp =[]
for info in order :
    temp = move_robot(info)
    if len(temp) == 1:
        print("Robot "+str(temp[0])+" crashes into the wall")
        break
    elif len(temp)==2:
        print("Robot "+ str(temp[0])+" crashes into robot "+ str(temp[1]))
        break
if temp ==[] : print("OK")





