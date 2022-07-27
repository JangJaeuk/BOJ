import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * i for i in range(1, n+1)]
    dp[0][0] = a[0][0]
    for i in range(1, n):
        dp[i][0] = a[i][0] + dp[i-1][0]
        dp[i][i] = a[i][i] + dp[i-1][i-1]
        
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = a[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    print(max(dp[n-1]))