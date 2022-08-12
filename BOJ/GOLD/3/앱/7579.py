import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    m = [0] + list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))
    MAX_C = sum(c)
    dp = [[0] * (MAX_C + 1) for _ in range(N+1)]
    res = MAX_C
    
    for i in range(1, N+1):
        byte = m[i]
        cost = c[i]
        for j in range(1, MAX_C+1):
            if j < cost:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-cost] + byte, dp[i-1][j])
            if dp[i][j] >= M:
                res = min(res, j)
    print(res)
    