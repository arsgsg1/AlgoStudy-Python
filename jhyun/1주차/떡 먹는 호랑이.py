D, K = map(int, input().split())
def solve():
    global D, K
    for A in range(1, K):
        for B in range(A, K):
            if A + B > K: break
            dp = [0] * D
            dp[0], dp[1] = A, B
            for k in range(2, D):
                dp[k] = dp[k - 1] + dp[k - 2]
            if dp[D - 1] == K:
                print(A)
                print(B)
                return
solve()