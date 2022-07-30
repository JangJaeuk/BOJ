import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    boxes = list(map(int, input().split()))
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if boxes[i] > boxes[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))
    