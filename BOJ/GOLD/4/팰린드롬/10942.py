# 팰린드롬

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
        
    for i in range(n-1):
        if a[i] == a[i+1]:
            dp[i][i+1] = 1
            
    for i in range(2, n):
        for j in range(n-i):
            if a[j] == a[i+j] and dp[j+1][i+j-1] == 1:
                dp[j][i+j] = 1
         
    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        print(dp[s-1][e-1])