N = int(input())
arr, q = [], []
colors, answer = [0] * (N + 1), [0] * N
total = 0
for i in range(N):
    c, s = map(int, input().split())
    arr.append((i, c, s))
arr.sort(key=lambda x: (x[2], x[1], x[0]))
total = 0
j = 0 # 크기를 위한 인덱스 변수
for i in range(N):
    a = arr[i]
    b = arr[j]
    while b[2] < a[2]: #크기가 같은 공을 건너뜀
        total += b[2]
        colors[b[1]] += b[2]
        j += 1
        b = arr[j]
    answer[a[0]] = total - colors[a[1]]

for item in answer:
    print(item)