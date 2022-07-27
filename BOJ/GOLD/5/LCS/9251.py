# lcs 구하는 문제 나중에 다시 볼 것!

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    s1 = input().rstrip()
    s2 = input().rstrip()
    s1_size, s2_size = len(s1), len(s2)
    dp = [[0] * (s2_size+1) for _ in range(s1_size+1)]
    
    for i in range(1, s1_size+1):
        for j in range(1, s2_size+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[-1][-1])
        
        