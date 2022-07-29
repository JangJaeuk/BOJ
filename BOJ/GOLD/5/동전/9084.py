import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        coins = list(map(int, input().split()))
        tm = int(input())
        dp = [0] * (tm + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, tm+1):
                if i >= coin:
                    dp[i] += dp[i-coin]
        print(dp[tm])