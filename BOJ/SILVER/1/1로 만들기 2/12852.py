# 1로 만들기

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)
    history_list = list(range(n+1))
    history_list[1] = 0 
  
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        history_list[i] = i-1
        
        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i//2] + 1
            history_list[i] = i // 2
        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i//3] + 1
            history_list[i] = i // 3

    while n != 0:
        print(n, end =' ')
        n = history_list[n]
    