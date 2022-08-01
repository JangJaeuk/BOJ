import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    schedule_list = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n+1)
    
    for i in range(n-1, -1, -1):
        if i + schedule_list[i][0] > n:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], schedule_list[i][1] + dp[i + schedule_list[i][0]])
            
    print(dp[0])