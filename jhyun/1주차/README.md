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
