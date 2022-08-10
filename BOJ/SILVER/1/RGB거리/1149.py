import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = map(int, input().split())
    
    for i in range(1, n):
        r, g, b = map(int, input().split())
        
        # r
        dp[i][0] = r + min(dp[i-1][1], dp[i-1][2])
        # g
        dp[i][1] = g + min(dp[i-1][0], dp[i-1][2])
        # b
        dp[i][2] = b + min(dp[i-1][0], dp[i-1][1])
        
    print(min(dp[n-1]))
    