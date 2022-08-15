import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n, t = map(int, input().split())
    dp = [0] * (t+1)
    
    for _ in range(n):
        k, s = map(int, input().split())
        for i in range(t, -1, -1):
            if i >= k:
                dp[i] = max(dp[i], dp[i-k] + s)
    print(dp[t])
        