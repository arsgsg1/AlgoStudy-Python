## 떡 먹는 호랑이
![image](https://user-images.githubusercontent.com/25299428/158106448-9bbc320d-5cb1-452f-b9ef-d985104062b3.png)

### 문제 접근
1. 첫째날과 둘째날의 떡 개수를 변화시키면서 dp를 적용시킬 수 있음
2. dp[i] = i번째 날에 준 떡 개수, dp[i] = dp[i - 1] + dp[i - 2]
3. top down, bottom up 두 가지 방식으로 해결할 수 있음
## 빵집
![image](https://user-images.githubusercontent.com/25299428/158167679-0a631767-5f74-4da9-aa9a-c620458b7ffe.png)

### 문제 접근
1. 우상향으로 먼저 파이프를 연결해야 최적의 파이프 연결을 할 수 있다.
2. 이미 찾은 경로를 다시 탐색할 필요가 없는게 핵심. visit 배열에 기록해두고 재방문하지 않도록 함.
3. 파이프를 연결했다면, 다음 로직을 실행하지 않고 끝내버리기 위해 반복문 안에서 조건을 만족하면 True를 반환함
## 테트로노미노
![image](https://user-images.githubusercontent.com/25299428/158380132-82e358ab-9a40-49de-8bf3-0ade77dad0a9.png)

### 문제 접근
1. N 크기가 500이기 때문에 모든 경우를 찾아도 시간 초과 X
2. 회전, 대칭하는 함수를 별도로 구현함
3. 격자에 3칸만큼 여유를 두어 4x4의 칸 안에 블럭을 회전, 대칭하여 점수를 계산할 수 있도로 함
## 컬러볼
### 문제 접근
1. N이 20만이기 때문에, 완전탐색으로는 풀 수 없음.
2. NlogN의 복잡도로 낮추기 위해 정렬하여 크기가 작은 공이 얻을 수 있는 점수를 구할 수 있음.
3. 이 때, 이전에 구했던 합을 재사용하기 위해 지금까지의 누적합 (색깔별, 총 크기별)을 함.
  3.1 i번째 공이 얻을 수 있는 점수 합 = 누적 점수 합 - i번째 공 색깔의 점수 합
4. 크기가 같은 공을 구분하기 위해 별도의 인덱스 그전과 크기가 다른 공이 나오면, 한 칸씩 건너뛰어 접근
## 순회 강연
![image](https://user-images.githubusercontent.com/25299428/159203758-9a064fdb-0d2b-481f-b7cb-7216c70565be.png)
### 문제 접근
d를 오름차, p를 내림차순으로 정렬하여 답을 구하려 했으나 틀렸다.
정답을 참조한 문제였는데, 핵심 아이디어는 1~d일 안에 가능한 강의들부터 채워나가는 그리디한 방법이다.
visit로 이미 강의를 채웠다면 다른 가능한 날을 찾도록 했다.
## Puyo Puyo
### 문제 접근
1. 중력
  - 맨 아래부터 뿌요라면 큐에 넣고, 빈 칸이라면 넘어감.
  - 아래부터 위로 큐에 원소가 있다면 해당 원소를 저장, 없다면 빈 칸으로 저장
2. bfs
  - 같은 색이고 상하좌우 인접한 뿌요만 탐색하여 좌표들을 큐에 저장
  - 큐 사이즈가 4이상이라면, 해당 칸을 빈칸으로 저장
## 상어 초등학교
![image](https://user-images.githubusercontent.com/25299428/159214485-cc1a03b1-72e5-4ace-a0d3-2c29917a9921.png)

### 문제 접근
- 학생을 순서대로 탐색
  - 왼쪽 상단부터 오른쪽 하단까지 탐색
    - 좋아하는 학생 수, 빈 칸 수별로 내림차순 행, 열 오름차순으로 정렬하여 칸을 우선순위 큐에 넣음
    - 우선순위 큐에서 원소 하나를 빼서 자리를 배치
