import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * n
    for i in range(n):
        dp[i] = a[i]
    
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], a[i] + dp[j])

    print(max(dp))