# 합분해 2

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[0][0] = 1
        
    for i in range(n+1):
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
             
    print(dp[n][k])